import { createBrowserRouter } from "react-router-dom"
import App from "./App";

import { Pokemon } from './pages/Pokemon';
import { Home } from './pages/home';
import { Moves } from './pages/moves';
import { RegisterPage } from "./pages/RegisterPage";
import { NotFoundPage } from "./pages/NotFoundPage";

const router = createBrowserRouter([
    {
        path: '/',
        element: <App />,
        children: [
            {
                index: true,
                element: <Home />

            },
            {
                path: "register/",
                element: <RegisterPage/>,
            },
            {
                path: "pokemon/",
                element: <Pokemon/>,
            },
            {
                path: "moves/",
                element: <Moves />,

            },
        ],
        errorElement: <NotFoundPage />
    } 
]);

export default router
