import {
  Box,
  Button,
  Card,
  PasswordInput,
  TextInput,
  Title,
  Stack,
  Group,
} from '@mantine/core';
import { useForm } from '@mantine/form';
import { notifications } from '@mantine/notifications';
import { useEffect, useState } from 'react';

interface UserData {
  email: string;
  username: string;
}

export default function Settings() {
  const [userData, setUserData] = useState<UserData | null>(null);
  const [isEditing, setIsEditing] = useState(false);

  const userForm = useForm({
    initialValues: {
      fullName: '',
      email: '',
    },
    validate: {
      email: (value) =>
        /^\S+@\S+$/.test(value) ? null : 'Geçersiz email adresi',
      fullName: (value) =>
        value.length < 2 ? 'İsim en az 2 karakter olmalıdır' : null,
    },
  });

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/auth/verify', {
          credentials: 'include',
        });

        if (!response.ok) {
          throw new Error('Kullanıcı bilgileri alınamadı');
        }

        const data = await response.json();
        setUserData(data);

        userForm.setValues({
          fullName: data.username,
          email: data.email,
        });
      } catch (error) {
        console.error('Veri çekme hatası:', error);
      }
    };

    fetchUserData();
  }, []);

  const passwordForm = useForm({
    initialValues: {
      currentPassword: '',
      newPassword: '',
      confirmPassword: '',
    },
    validate: {
      currentPassword: (value) =>
        value.length < 6 ? 'Şifre en az 6 karakter olmalıdır' : null,
      newPassword: (value) =>
        value.length < 6 ? 'Şifre en az 6 karakter olmalıdır' : null,
      confirmPassword: (value, values) =>
        value !== values.newPassword ? 'Şifreler eşleşmiyor' : null,
    },
  });

  const handleUserUpdate = async (values: typeof userForm.values) => {
    console.log(values);

    try {
      const res = await fetch('http://127.0.0.1:5000/api/update-user', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({
          username: values.fullName,
          email: values.email,
        }),
      });
      if (res.ok) {
        notifications.show({
          title: 'İşlem Başarılı',
          message: 'Bilgileriniz güncellendi',
          position: 'bottom-center',
          withCloseButton: false,
        });
        console.log('Kullanıcı bilgileri güncellendi');
      }
      console.log('Kullanıcı bilgileri güncelleniyor:', values);
      setIsEditing(false); // Başarılı güncelleme sonrası edit modunu kapat
    } catch (error) {
      console.error('Güncelleme hatası:', error);
    }
  };

  const handleCancelEdit = () => {
    // İptal edildiğinde orijinal değerlere geri dön
    if (userData) {
      userForm.setValues({
        fullName: userData.username,
        email: userData.email,
      });
    }
    setIsEditing(false);
  };

  const handlePasswordUpdate = async (values: typeof passwordForm.values) => {
    const res = await fetch('http://127.0.0.1:5000/api/change-password', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: 'include',
      body: JSON.stringify({
        current_password: values.currentPassword,
        new_password: values.newPassword,
      }),
    });
    if (res.ok) {
      notifications.show({
        title: 'İşlem Başarılı',
        message: 'Şifreniz güncellendi',
        position: 'bottom-center',
        withCloseButton: false,
      });
      passwordForm.reset();
    } else if (res.status === 400) {
      notifications.show({
        title: 'İşlem Basarisiz',
        message: 'Mevcut sifreniz yanlis',
        position: 'bottom-center',
        withCloseButton: false,
      });
    }
    // Şifre güncelleme işlemi burada yapılacak
    console.log('Şifre güncelleniyor:', values);
  };

  return (
    <Box p="md">
      <Title order={2} mb="lg">
        Ayarlar
      </Title>

      <Card withBorder mb="lg">
        <Title order={3} mb="md">
          Profil Bilgileri
        </Title>
        <form onSubmit={userForm.onSubmit(handleUserUpdate)}>
          <Stack>
            <TextInput
              label="Kullanıcı Adı"
              placeholder="Kullanıcı adınızı giriniz"
              {...userForm.getInputProps('fullName')}
              disabled={!isEditing}
            />
            <TextInput
              label="E-posta"
              placeholder="E-posta adresinizi giriniz"
              {...userForm.getInputProps('email')}
              disabled={!isEditing}
            />
            <Group justify="flex-start">
              {!isEditing ? (
                <Button onClick={() => setIsEditing(true)}>Düzenle</Button>
              ) : (
                <>
                  <Button variant="light" onClick={handleCancelEdit}>
                    İptal
                  </Button>
                  <Button type="submit">Kaydet</Button>
                </>
              )}
            </Group>
          </Stack>
        </form>
      </Card>

      <Card withBorder>
        <Title order={3} mb="md">
          Şifre Değiştir
        </Title>
        <form onSubmit={passwordForm.onSubmit(handlePasswordUpdate)}>
          <Stack>
            <PasswordInput
              label="Mevcut Şifre"
              placeholder="Mevcut şifrenizi giriniz"
              {...passwordForm.getInputProps('currentPassword')}
            />
            <PasswordInput
              label="Yeni Şifre"
              placeholder="Yeni şifrenizi giriniz"
              {...passwordForm.getInputProps('newPassword')}
            />
            <PasswordInput
              label="Yeni Şifre (Tekrar)"
              placeholder="Yeni şifrenizi tekrar giriniz"
              {...passwordForm.getInputProps('confirmPassword')}
            />
            <Group justify="flex-start">
              <Button type="submit">Şifreyi Güncelle</Button>
            </Group>
          </Stack>
        </form>
      </Card>
    </Box>
  );
}
