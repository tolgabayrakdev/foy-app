import React, { useState } from 'react';
import { TextInput, PasswordInput, Button, Anchor, Paper, Title, Flex, Container, Alert } from '@mantine/core';
import { useForm } from '@mantine/form';
import { useNavigate } from 'react-router';
import { AlertCircle } from 'lucide-react';

const SignUp = () => {
    const navigate = useNavigate();
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const form = useForm({
        initialValues: {
            username: '',
            email: '',
            password: '',
        },
        validate: {
            username: (value) => (value.length >= 3 ? null : 'Kullanıcı adı en az 3 karakter olmalı'),
            email: (value) => (/\S+@\S+\.\S+/.test(value) ? null : 'Geçersiz email'),
            password: (value) => (value.length >= 6 ? null : 'Şifre en az 6 karakter olmalı'),
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
            const response = await fetch('http://127.0.0.1:5000/api/auth/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: form.values.username,
                    email: form.values.email,
                    password: form.values.password,
                }),
            });
            const data = await response.json();


            if (response.ok) {
                // Kayıt olma başarılı
                navigate('/sign-in');
            } else {
                setError(data.message || 'Kayıt olma sırasında bir hata oluştu');
            }
        } catch (error) {
            setError('Kayıt olma sırasında bir hata oluştu');
        } finally {
            setLoading(false);
        }

    };

    return (
        <Flex
            justify="center"
            align="center"
            style={{ minHeight: '100vh' }}
        >
            <Container size={420} w="100%">
                <Paper p="lg" radius="md">
                    <Title ta="center" mb={30}>Kayıt Ol</Title>

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
                            label="Kullanıcı Adı"
                            placeholder="username"
                            required
                            {...form.getInputProps('username')}
                        />

                        <TextInput
                            label="Email"
                            placeholder="youremail@example.com"
                            required
                            mt="md"
                            {...form.getInputProps('email')}
                        />

                        <PasswordInput
                            label="Şifre"
                            placeholder="Şifrenizi girin"
                            required
                            mt="md"
                            {...form.getInputProps('password')}
                        />

                        <Button loading={loading} fullWidth mt="xl" type="submit">Kayıt Ol</Button>
                    </form>

                    <Anchor
                        ta="center"
                        href="/sign-in"
                        mt="sm"
                        size="sm"
                        style={{ display: 'block', textAlign: 'center' }}
                    >
                        Zaten bir hesabın var mı? Giriş yap
                    </Anchor>
                </Paper>
            </Container>
        </Flex>
    );
};

export default SignUp;