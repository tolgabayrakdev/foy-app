import { createRoot } from 'react-dom/client'
import './index.css'
import '@mantine/core/styles.css';
import { RouterProvider } from 'react-router-dom'
import routes from './routes'
import { Suspense } from 'react'
import Loading from './components/loading'
import { MantineProvider } from '@mantine/core'

createRoot(document.getElementById('root')!).render(
  <MantineProvider>
    <Suspense fallback={<Loading />}>
      <RouterProvider router={routes} future={{ v7_startTransition: true }} />
    </Suspense>
  </MantineProvider>

)
