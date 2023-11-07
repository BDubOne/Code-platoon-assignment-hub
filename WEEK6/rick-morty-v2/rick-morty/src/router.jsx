import { createBrowserRouter } from 'react-router-dom'
import App from './App'
import HomePage from './pages/HomePage'
import CharactersPage from './pages/CharactersPage'
import NotFoundPage from './pages/NotFoundPage'
import AboutPage from './pages/AboutPage'


const router = createBrowserRouter([
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
                path: 'characters/',
                element: <CharactersPage />
            }
        ],
        errorElement: <NotFoundPage />
    }
])

export default router