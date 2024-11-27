import { Button, Flex, Paper, Text } from "@mantine/core"
import { useNavigate } from "react-router";

export default function Home() {
  const navigate = useNavigate();

  return (
    <Flex
      justify="center"
      align="center"
      style={{ minHeight: '100vh' }}
      direction="column"
    >
      <Text size="xl">Hoşgeldin</Text>
      <Paper p="xs">
        <Button onClick={() => navigate('/sign-in')} variant="default" mr="3">Giriş Yap</Button>
        <Button onClick={() => navigate('/sign-up')} variant="default">Kayıt Ol</Button>
      </Paper>

    </Flex>
  )
}
