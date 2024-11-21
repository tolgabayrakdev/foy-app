import { Flex, Loader, Text } from "@mantine/core";

export default function loading() {
  return (
    <Flex
      pos="fixed"
      top="0"
      left="0"
      right="0"
      bottom="0"
      bg="white"
      justify="center"
      align="center"
      style={{ zIndex: 1000 }}
    >
      <Flex 
        align="center" 
        gap="xs"
      >
        <Loader size="xs" />
        <Text c="gray" size="sm">
          Yükleniyor...
        </Text>
      </Flex>
    </Flex>
  )
}
