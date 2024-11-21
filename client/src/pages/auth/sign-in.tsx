import React from 'react';
import { TextInput, PasswordInput, Button, Anchor, Paper, Title, Container, Flex } from '@mantine/core';
import { useForm } from '@mantine/form';

const SignIn = () => {
    // Form yönetimi için useForm kullanıyoruz
    const form = useForm({
        initialValues: {
            email: '',
            password: '',
        },
        validate: {
            email: (value) => (/\S+@\S+\.\S+/.test(value) ? null : 'Geçersiz email'),
            password: (value) => (value.length >= 6 ? null : 'Şifre en az 6 karakter olmalı'),
        },
    });

    // Login işlemi burada yapılacak
    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        if (form.validate().hasErrors) {
            return;
        }
        // Burada backend'e API çağrısı yapılabilir
        console.log('Email:', form.values.email);
        console.log('Password:', form.values.password);
    };

    return (
        <Flex
            justify="center"
            align="center"
            style={{ minHeight: '100vh' }}
        >
            <Container size={420} w="100%">
                <Paper p="lg" radius="md">
                    <Title ta="center" mb={30}>Giriş Yap</Title>

                    <form onSubmit={handleSubmit}>
                        <TextInput
                            label="Email"
                            placeholder="youremail@example.com"
                            required
                            {...form.getInputProps('email')}
                        />

                        <PasswordInput
                            label="Şifre"
                            placeholder="Şifrenizi girin"
                            required
                            mt="md"
                            {...form.getInputProps('password')}
                        />

                        <Button fullWidth mt="xl" type="submit">Giriş Yap</Button>
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