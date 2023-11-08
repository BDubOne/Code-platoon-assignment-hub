import { createBrowserRouter } from 'react-router-dom'
import App from './App'
import AboutPage from './pages/AboutPage'
import CharactersPage from './pages/CharactersPage'
import NotFoundPage from './pages/NotFoundPage'
import HomePage from './pages/HomePage'
import SingleCharacterPage from './pages/SingleCharPage'


const router = createBrowserRouter([
    {
        path:'/',
        element: <App />,
        children: [
            {
                index: true,
                element: <HomePage />
            },
            {
                path: 'about/',
                element: <AboutPage />

            },
            {
                path:'characters/',
                element: <CharactersPage />
            },
            {
                path:'characters/:id',
                element: <SingleCharacterPage />
            },

        ],
        errorElement:<NotFoundPage />
    },
]);

export default router