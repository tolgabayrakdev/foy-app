import { TextInput, PasswordInput, Button, Paper, Stack, Title, Box, Text, Divider } from '@mantine/core';
import { useForm } from '@mantine/form';
import { notifications } from '@mantine/notifications';
import { KeyIcon, LockIcon, MailIcon, User2Icon } from 'lucide-react';
import { useState, useEffect } from 'react';

interface UserInfo {
  username: string;
  email: string;
}

interface PasswordChange {
  currentPassword: string;
  newPassword: string;
  confirmPassword: string;
}

function Settings() {
  const [loading, setLoading] = useState(false);
  
  const userForm = useForm<UserInfo>({
    initialValues: {
      username: '',
      email: '',
    },
    validate: {
      email: (value) => (/^\S+@\S+$/.test(value) ? null : 'Geçersiz email'),
      username: (value) => (value.length < 3 ? 'Kullanıcı adı en az 3 karakter olmalıdır' : null),
    },
  });

  const passwordForm = useForm<PasswordChange>({
    initialValues: {
      currentPassword: '',
      newPassword: '',
      confirmPassword: '',
    },
    validate: {
      newPassword: (value) => (value.length < 6 ? 'Şifre en az 6 karakter olmalıdır' : null),
      confirmPassword: (value, values) =>
        value !== values.newPassword ? 'Şifreler eşleşmiyor' : null,
    },
  });

  useEffect(() => {
    const fetchUserInfo = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/auth/verify', {
          credentials: 'include',
        });
        const data = await response.json();
        if (response.ok) {
          userForm.setValues({
            username: data.username,
            email: data.email,
          });
        }
      } catch (error) {
        console.error('Kullanıcı bilgileri yüklenemedi:', error);
      }
    };
    fetchUserInfo();
  }, []);

  const handleUpdateProfile = async (values: UserInfo) => {
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:5000/api/auth/update-profile', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(values),
      });

      if (response.ok) {
        notifications.show({
          title: 'Başarılı',
          message: 'Profil bilgileri güncellendi',
          color: 'green',
        });
      } else {
        const error = await response.json();
        throw new Error(error.message);
      }
    } catch (error) {
      notifications.show({
        title: 'Hata',
        message: 'Profil güncellenirken bir hata oluştu',
        color: 'red',
      });
    } finally {
      setLoading(false);
    }
  };

  const handleChangePassword = async (values: PasswordChange) => {
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:5000/api/auth/change-password', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({
          current_password: values.currentPassword,
          new_password: values.newPassword,
        }),
      });

      if (response.ok) {
        notifications.show({
          title: 'Başarılı',
          message: 'Şifre başarıyla değiştirildi',
          color: 'green',
        });
        passwordForm.reset();
      } else {
        const error = await response.json();
        throw new Error(error.message);
      }
    } catch (error) {
      notifications.show({
        title: 'Hata',
        message: 'Şifre değiştirilirken bir hata oluştu',
        color: 'red',
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box mx="auto" px="md" maw={800}>
      <Title order={1} mb="lg">Hesap Ayarları</Title>
      <Stack gap="lg">
        <Paper p="xl" withBorder>
          <Stack>
            <Box mb="md">
              <Title order={2} size="h3" mb={5}>
                <User2Icon size={20} style={{ marginRight: 10, display: 'inline' }} />
                Profil Bilgileri
              </Title>
              <Text c="dimmed" size="sm">
                Kişisel bilgilerinizi buradan güncelleyebilirsiniz
              </Text>
            </Box>
            <Divider mb="sm" />
            <form onSubmit={userForm.onSubmit(handleUpdateProfile)}>
              <Stack>
                <TextInput
                  label="Kullanıcı Adı"
                  placeholder="Kullanıcı adınız"
                  leftSection={<User2Icon size={16} />}
                  {...userForm.getInputProps('username')}
                />
                <TextInput
                  label="Email"
                  placeholder="Email adresiniz"
                  leftSection={<MailIcon size={16} />}
                  {...userForm.getInputProps('email')}
                />
                <Button 
                  type="submit" 
                  loading={loading}
                  fullWidth
                  mt="md"
                >
                  Profili Güncelle
                </Button>
              </Stack>
            </form>
          </Stack>
        </Paper>

        <Divider />

        <Paper p="xl" withBorder>
          <Stack>
            <Box mb="md">
              <Title order={2} size="h3" mb={5}>
                <LockIcon size={20} style={{ marginRight: 10, display: 'inline' }} />
                Şifre Değiştir
              </Title>
              <Text c="dimmed" size="sm">
                Hesap güvenliğiniz için şifrenizi düzenli olarak değiştirin
              </Text>
            </Box>
            <Divider mb="sm" />
            <form onSubmit={passwordForm.onSubmit(handleChangePassword)}>
              <Stack>
                <PasswordInput
                  label="Mevcut Şifre"
                  placeholder="Mevcut şifreniz"
                  leftSection={<KeyIcon size={16} />}
                  {...passwordForm.getInputProps('currentPassword')}
                />
                <PasswordInput
                  label="Yeni Şifre"
                  placeholder="Yeni şifreniz"
                  leftSection={<KeyIcon size={16} />}
                  {...passwordForm.getInputProps('newPassword')}
                />
                <PasswordInput
                  label="Yeni Şifre Tekrar"
                  placeholder="Yeni şifrenizi tekrar girin"
                  leftSection={<KeyIcon size={16} />}
                  {...passwordForm.getInputProps('confirmPassword')}
                />
                <Button 
                  type="submit" 
                  loading={loading}
                  fullWidth
                  mt="md"
                >
                  Şifreyi Değiştir
                </Button>
              </Stack>
            </form>
          </Stack>
        </Paper>
      </Stack>
    </Box>
  );
}

export default Settings;