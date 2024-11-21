import React from 'react';
import { TextInput, PasswordInput, Button, Anchor, Paper, Title, Container } from '@mantine/core';
import { useForm } from '@mantine/form';

const SignIn = () => {
    // Form yönetimi için useForm kullanıyoruz
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

    // Login işlemi burada yapılacak
    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        if (form.validate().hasErrors) {
            return;
        }
        // Burada backend'e API çağrısı yapılabilir
        console.log('Username:', form.values.username);
        console.log('Email:', form.values.email);
        console.log('Password:', form.values.password);
    };

    return (
        <Container size={420} my={40}>
            <Paper>
                <Title ta="center" mb={30}>Giriş Yap</Title>

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

                    <Button fullWidth mt="xl" type="submit">Giriş Yap</Button>
                </form>

                <Anchor ta="center" href="/sign-in" mt="sm" size="sm" display="block">
                    Zaten bir hesabın var mı?
                </Anchor>
            </Paper>
        </Container>
    );
};

export default SignIn;
