import { lazy } from "react";
import { createBrowserRouter } from "react-router-dom";

const HomePage = lazy(() => import("./pages/home"));
const NotFoundPage = lazy(() => import("./pages/error/not-found"));
const SignInPage = lazy(() => import("./pages/auth/sign-in"));
const SignUpPage = lazy(() => import("./pages/auth/sign-up"));

const MainLayout = lazy(() => import("./layouts/main-layout"));
const MainIndexPage = lazy(() => import("./pages/main/index"));
const MainSettingsPage = lazy(() => import("./pages/main/settings"));

const routes = createBrowserRouter([
    {
        path: "/",
        element: <HomePage />
    },
    {
        path: "*",
        element: <NotFoundPage />
    },
    {
        path: "/sign-in",
        element: <SignInPage />
    },
    {
        path: "/sign-up",
        element: <SignUpPage />
    },
    {
        path: "/main",
        element: <MainLayout />,
        children: [
            { path: "", element: <MainIndexPage />, index: true },
            { path: "settings", element: <MainSettingsPage /> }
        ]
    }
], {
    future: {
        v7_fetcherPersist: true,
        v7_normalizeFormMethod: true,
        v7_partialHydration: true,
        v7_relativeSplatPath: true,
        v7_skipActionErrorRevalidation: true
    }
});

export default routes;