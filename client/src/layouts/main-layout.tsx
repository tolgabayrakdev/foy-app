import { AppShell, Burger, Group, Title, Menu, Button, rem, NavLink } from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';
import { IconSettings, IconLogout, IconUsers, IconNotes, IconHome } from '@tabler/icons-react';
import { useNavigate, useLocation, Outlet } from 'react-router-dom';

export default function MainLayout() {
  const [mobileOpened, { toggle: toggleMobile }] = useDisclosure();
  const [desktopOpened, { toggle: toggleDesktop }] = useDisclosure(true);
  const navigate = useNavigate();
  const location = useLocation();
  
  const userEmail = "kullanici@email.com";

  const handleLogout = () => {
    console.log("Çıkış yapılıyor...");
  };

  const navItems = [
    {
      label: 'Main',
      path: '/main',
      icon: <IconHome style={{ width: rem(16), height: rem(16) }} />
    },
    {
      label: 'Kullanıcılar',
      path: '/users',
      icon: <IconUsers style={{ width: rem(16), height: rem(16) }} />
    },
    {
      label: 'Notlar',
      path: '/notes',
      icon: <IconNotes style={{ width: rem(16), height: rem(16) }} />
    },
    {
      label: 'Ayarlar',
      path: '/main/settings',
      icon: <IconSettings style={{ width: rem(16), height: rem(16) }} />
    }
  ];

  return (
    <AppShell
      header={{ height: 50 }}
      navbar={{
        width: 250,
        breakpoint: 'sm',
        collapsed: { mobile: !mobileOpened, desktop: !desktopOpened },
      }}
      padding="md"
    >
      <AppShell.Header>
        <Group h="100%" px="md" justify="space-between">
          <Group>
            <Burger opened={mobileOpened} onClick={toggleMobile} hiddenFrom="sm" size="sm" />
            <Burger opened={desktopOpened} onClick={toggleDesktop} visibleFrom="sm" size="sm" />
            <Title order={2}>Foy</Title>
          </Group>

          <Menu shadow="md" width={200}>
            <Menu.Target>
              <Button variant="subtle">
                {userEmail}
              </Button>
            </Menu.Target>

            <Menu.Dropdown>
              <Menu.Item
                leftSection={<IconSettings style={{ width: rem(14), height: rem(14) }} />}
                onClick={() => navigate('/settings')}
              >
                Ayarlar
              </Menu.Item>
              
              <Menu.Item
                leftSection={<IconLogout style={{ width: rem(14), height: rem(14) }} />}
                onClick={handleLogout}
                color="red"
              >
                Çıkış Yap
              </Menu.Item>
            </Menu.Dropdown>
          </Menu>
        </Group>
      </AppShell.Header>
      <AppShell.Navbar p="md">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            label={item.label}
            leftSection={item.icon}
            active={location.pathname === item.path}
            onClick={() => navigate(item.path)}
            styles={{
              root: {
                '&[data-active]': {
                  backgroundColor: 'var(--mantine-primary-color-light)',
                }
              }
            }}
          />
        ))}
      </AppShell.Navbar>
      <AppShell.Main>
        <Outlet />
      </AppShell.Main>
    </AppShell>
  );
}
