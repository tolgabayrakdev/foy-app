import { Suspense } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { RouterProvider } from 'react-router-dom'
import routes from './routes'
import Loading from './components/loading'

createRoot(document.getElementById('root')!).render(
  <Suspense fallback={<Loading />}>
    <RouterProvider future={{ v7_startTransition: true }} router={routes} />
  </Suspense>
)
