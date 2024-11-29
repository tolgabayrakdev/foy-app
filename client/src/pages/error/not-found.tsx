import { Button, Flex, Text } from '@mantine/core';
import { useNavigate } from 'react-router';

export default function NotFound() {
  const navigate = useNavigate();
  return (
    <Flex
      justify="center"
      align="center"
      direction="column"
      style={{ minHeight: '100vh' }}
    >
      <Text size="xl">404 Not Found</Text>
      <Button variant="white" onClick={() => navigate(-1)}>
        Geri Dön
      </Button>
    </Flex>
  );
}
