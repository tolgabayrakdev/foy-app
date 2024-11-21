import { createRoot } from 'react-dom/client'
import './index.css'
import '@mantine/core/styles.css';
import { RouterProvider } from 'react-router-dom'
import routes from './routes'
import { Suspense } from 'react'
import { MantineProvider } from '@mantine/core'
import Loading from './components/Loading';

createRoot(document.getElementById('root')!).render(
  <MantineProvider>
    <Suspense fallback={<Loading />}>
      <RouterProvider router={routes} future={{ v7_startTransition: true }} />
    </Suspense>
  </MantineProvider>

)
