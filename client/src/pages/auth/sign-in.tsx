import React, { useState } from 'react';
import {
  TextInput,
  PasswordInput,
  Button,
  Anchor,
  Paper,
  Title,
  Container,
  Flex,
  Alert,
} from '@mantine/core';
import { useForm } from '@mantine/form';
import { useNavigate } from 'react-router';
import { AlertCircle } from 'lucide-react';

const SignIn = () => {
  const navigate = useNavigate();
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const form = useForm({
    initialValues: {
      email: '',
      password: '',
    },
    validate: {
      email: (value) => (/\S+@\S+\.\S+/.test(value) ? null : 'Geçersiz email'),
      password: (value) =>
        value.length >= 6 ? null : 'Şifre en az 6 karakter olmalı',
    },
  });

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    if (form.validate().hasErrors) {
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch('http://127.0.0.1:5000/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({
          email: form.values.email,
          password: form.values.password,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        // Başarılı login
        navigate('/main');
      } else {
        // Backend'den gelen hata mesajını göster
        setError(data.message || 'Email veya sifre yanlış');
      }
    } catch (err) {
      setError(`Sunucu hatası, detaylar: ${err}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Flex justify="center" align="center" style={{ minHeight: '100vh' }}>
      <Container size={420} w="100%">
        <Paper p="lg" radius="md">
          <Title ta="center" mb={30}>
            Giriş Yap
          </Title>

          {error && (
            <Alert
              icon={<AlertCircle size={16} />}
              color="red"
              mb="md"
              title="Hata"
            >
              {error}
            </Alert>
          )}

          <form onSubmit={handleSubmit}>
            <TextInput
              label="Email"
              placeholder="youremail@example.com"
              required
              {...form.getInputProps('email')}
              disabled={loading}
            />

            <PasswordInput
              label="Şifre"
              placeholder="Şifrenizi girin"
              required
              mt="md"
              {...form.getInputProps('password')}
              disabled={loading}
            />

            <Button fullWidth mt="xl" type="submit" loading={loading}>
              Giriş Yap
            </Button>
          </form>

          <Anchor
            ta="center"
            href="/sign-up"
            mt="sm"
            size="sm"
            style={{ display: 'block', textAlign: 'center' }}
          >
            Hesabınız yok mu? Kayıt olun
          </Anchor>
        </Paper>
      </Container>
    </Flex>
  );
};

export default SignIn;
