import { lazy } from "react";
import { createBrowserRouter } from "react-router-dom";
import NotFound from "./pages/NotFound";

const HomePage = lazy(() => import("./pages/Home"));


const routes = createBrowserRouter([
    {
        path: "*",
        element: <NotFound />
    },
    {
        path: "/",
        element: <HomePage />
    },
], {
    future: {
        v7_fetcherPersist: true,
        v7_normalizeFormMethod: true,
        v7_partialHydration: true,
        v7_relativeSplatPath: true,
        v7_skipActionErrorRevalidation: true
    }
}
);

export default routes;