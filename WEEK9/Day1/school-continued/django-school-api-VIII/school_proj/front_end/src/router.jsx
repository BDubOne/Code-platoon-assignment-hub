import { createBrowserRouter } from 'react-router-dom'
import App from './App'

import { Students } from './pages/students'
import { Home } from './pages/home'
import { SingleStudent} from './pages/single-student'
import { EditSingleStudent } from './pages/edit-single-student'
import { Subjects } from './pages/subjects'
import { SingleSubject } from './pages/single-subject'
import { NotFoundPage } from './pages/not-found-page'

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
                path: 'students/',
                element: <Students />
            },
            {
                path: 'students/:id/',
                element: <SingleStudent />
            },
            {
                path: 'students/:id/edit',
                element: <EditSingleStudent/>
            },
            {
                path: 'subjects/',
                element: <Subjects />
            },
            {
                path: 'subjects/:subject_name/',
                element: <SingleSubject />
            },
        ],
        errorElement: <NotFoundPage />
    }
]);

export default router