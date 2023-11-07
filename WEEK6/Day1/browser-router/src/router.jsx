import { createBrowserRouter, createHashRouter } from "react-router-dom";
import App from './App'
import HomePage from './pages/HomePage'
import ContactPage from './pages/ContactPage'
import AboutPage from "./pages/AboutPage"
import NotFoundPage from './pages/NotFoundPage'

const router = createHashRouter([
    {
        //http://localhost:5173/
        path: "/",
        element: <App/>,
        children: [
            {
                index: true,
                element: <HomePage/>
            },
            {
                path: 'about/',
                element: <AboutPage />
            },
            {
                path: 'contact/',
                element: <ContactPage />
            }
        ],
        errorElement: <NotFoundPage />
    }
])

export default router