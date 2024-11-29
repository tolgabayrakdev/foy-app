import { createRoot } from 'react-dom/client';
import './index.css';
import '@mantine/core/styles.css';
import '@mantine/notifications/styles.css';
import { lazy, Suspense } from 'react';
import { MantineProvider } from '@mantine/core';
import Loading from './components/loading';
import { BrowserRouter, Route, Routes } from 'react-router';
import { Notifications } from '@mantine/notifications';

const SignIn = lazy(() => import('./pages/auth/sign-in'));
const SignUp = lazy(() => import('./pages/auth/sign-up'));
const MainLayout = lazy(() => import('./layouts/main-layout'));
const MainIndex = lazy(() => import('./pages/main/index'));
const MainSettings = lazy(() => import('./pages/main/settings'));

const Home = lazy(() => import('./pages/home'));
const NotFound = lazy(() => import('./pages/error/not-found'));

createRoot(document.getElementById('root')!).render(
  <MantineProvider>
    <Suspense fallback={<Loading />}>
      <Notifications />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="*" element={<NotFound />} />
          <Route path="/sign-in" element={<SignIn />} />
          <Route path="/sign-up" element={<SignUp />} />

          <Route path="/main">
            <Route element={<MainLayout />}>
              <Route index element={<MainIndex />} />
              <Route path="settings" element={<MainSettings />} />
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </Suspense>
  </MantineProvider>,
);
