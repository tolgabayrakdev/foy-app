import { createRoot } from 'react-dom/client'
import './index.css'
import '@mantine/core/styles.css';
import { lazy, Suspense } from 'react'
import { MantineProvider } from '@mantine/core'
import Loading from './components/Loading';
import { BrowserRouter, Route, Routes } from 'react-router';

const Home = lazy(() => import('./pages/home'));
const NotFound = lazy(() => import('./pages/error/not-found'));
const SignIn = lazy(() => import('./pages/auth/sign-in'));
const SignUp = lazy(() => import('./pages/auth/sign-up'));
const MainLayout = lazy(() => import('./layouts/main-layout'));
const Index = lazy(() => import('./pages/main'));
const Settings = lazy(() => import('./pages/main/settings'));

createRoot(document.getElementById('root')!).render(
  <MantineProvider>
    <Suspense fallback={<Loading />}>
      <BrowserRouter>
        <Routes>
          <Route
            path='/' element={<Home />} />
          <Route path='*' element={<NotFound />} />
          <Route path='/sign-in' element={<SignIn />} />
          <Route path='/sign-up' element={<SignUp />} />

          <Route path='/main'>
            <Route element={<MainLayout />}>
              <Route index element={<Index />} />
              <Route path='settings' element={<Settings />} />
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </Suspense>
  </MantineProvider>

)
