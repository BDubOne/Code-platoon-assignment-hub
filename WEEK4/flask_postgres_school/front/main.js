//Here, we are defining the elements of the static page
function updateContent(navItem) {
    const title = document.getElementById('title');
    const subTitle = document.getElementById('sub-title');
    const contentList = document.getElementById('content');

//here, we are creating switchcases for the navbar so that the display can change on hover
    switch (navItem) {
        case 'students':
            title.textContent = 'Students';
            subTitle.textContent = 'Victor Cohort';
            contentList.innerHTML = '<li>Click to learn more about our current cohort!</li><li>We are a a fine assortment of active military members, veterans, and spouses!</li>';
            break;
        
        case 'faculty':
            title.textContent = 'Faculty';
            subTitle.textContent = 'Our Instructors';
            contentList.innerHTML = '<li>Get to know our instructors!</li><li>Some have gone through our program</li><li>All are experienced, capable, and committed to excellence!</li>';
            break;
        
        case 'programs':
            title.textContent='Programs';
            subTitle.textContent="What You'll Learn";
            contentList.innerHTML = '<li>Javascript</li><li>Python</li><li>Django</li><li>React</li><li>SQL</li><li>And Much More!</li>';
            console.log('students')
            break;
        
        case 'activities':
            title.textContent='Activities';
            subTitle.textContent="What You'll Do";
            contentList.innerHTML= '<li>Computer Logic</li><li>Web Design</li><li>Data Management</li><li>FullStack Development</li><li>And Much More!</li><li>navigate here to learn more!</li>';
     
            break;
           
        case 'contact':
            title.textContent='Contact';
            subTitle.textContent='Reach out to Our Amazing Team'
            contentList.innerHTML='<li>This may not be able to be an unordered list</li>'
         
            break;
        
        default:
            title.textContent = 'Code Platoon';
            subTitle.textContent = '(bootleg)';
            contentList.innerHTML = '<li>This is not the official Code Platoon WebPage</li><li>None of the information here</li><li>Corresponds to actual personal data</li>';
          

    }
}
//here we actually listen for the mouse to hover over the given text. By using 'mouseenter', the place that is hovered will remain until another item is hovered
document.addEventListener('DOMContentLoaded', function () {
    const navItems = document.querySelectorAll('.nav a');
    navItems.forEach((navItem) => {
        navItem.addEventListener('mouseenter', () => {
            const dataContent = navItem.getAttribute('data-content');
            updateContent(dataContent || '');
           
        });
    });
});

//This part of the JS begins to handle working with my Flask server to retrieve data
const getStudentNames = async() => {
    try {
        let response = await fetch('http://127.0.0.1:5000/students')
        if (!response.ok) {
            throw new Error('Network response not ok')
        }

        let data = await response.json()

        let ul = document.getElementById("content")
        ul.innerHTML = '';

        for (student of data) {     
            let li = document.createElement('li')
            li.innerText = `${student.first_name} ${student.last_name}`;
            ul.appendChild(li)
        
        }
    } catch (error) {
        console.error("Error", error);
    }
    
}

const getFaculty = async() => {

    try {
        let response = await fetch('http://127.0.0.1:5000/teachers')
        if (!response.ok) {
            throw new Error('Network response not ok')
        }

        let data = await response.json()

        let ul = document.getElementById("content")
        ul.innerHTML = '';

        for (teacher of data) {     
            let li = document.createElement('li')
            li.innerText = `${teacher.first_name} ${teacher.last_name}`;
            ul.appendChild(li)
        
        }
    } catch (error) {
        console.error("Error", error);
    }
}

const getPrograms = async() => {

    try {
        let response = await fetch('http://127.0.0.1:5000/subjects')
        if (!response.ok) {
            throw new Error('Network response not ok')
        }

        let data = await response.json()

        let ul = document.getElementById("content")
        ul.innerHTML = '';

        for (subject of data) {     
            let li = document.createElement('li')
            li.innerText = `${subject.subject} by  ${subject.teacher}`;
            ul.appendChild(li)
        
        }
    } catch (error) {
        console.error("Error", error);
    }
}


//this event listener is repetative, but it is designed to handle clicks, which will trigger interaction with the flask server connected to the sql database
document.addEventListener('DOMContentLoaded', function() {
    const navItems = document.querySelectorAll('.nav a');
  

    navItems.forEach((navItem) => {
        navItem.addEventListener('click', async (event) => {
            event.preventDefault();
            const dataContent = navItem.getAttribute('data-content');

            if (dataContent === 'students') {

               getStudentNames();
            }
            else if (dataContent === 'faculty') {
                getFaculty();
            }
            else if (dataContent === 'programs') {
                getPrograms();
            }

            });
        });
    });


// //Here, we are defining the elements of the static page
// function updateContent(navItem) {
//     const title = document.getElementById('title');
//     const subTitle = document.getElementById('sub-title');
//     const contentList = document.getElementById('content');

// //here, we are creating switchcases for the navbar so that the display can change on hover
//     switch (navItem) {
//         case 'students':
//             title.textContent = 'Students';
//             subTitle.textContent = 'Victor Cohort';
//             contentList.innerHTML = '<li>Click to learn more about our current cohort!</li><li>We are a a fine assortment of active military members, veterans, and spouses!</li>';
//             break;
        
//         case 'faculty':
//             title.textContent = 'Faculty';
//             subTitle.textContent = 'Our Instructors';
//             contentList.innerHTML = '<li>Get to know our instructors!</li><li>Some have gone through our program</li><li>All are experienced, capable, and committed to excellence!</li>';
//             break;
        
//         case 'programs':
//             title.textContent='Programs';
//             subTitle.textContent="What You'll Learn";
//             contentList.innerHTML = '<li>Javascript</li><li>Python</li><li>Django</li><li>React</li><li>SQL</li><li>And Much More!</li>';
//             console.log('students')
//             break;
        
//         case 'activities':
//             title.textContent='Activities';
//             subTitle.textContent="What You'll Do";
//             contentList.innerHTML= '<li>Computer Logic</li><li>Web Design</li><li>Data Management</li><li>FullStack Development</li><li>And Much More!</li><li>navigate here to learn more!</li>';
     
//             break;
           
//         case 'contact':
//             title.textContent='Contact';
//             subTitle.textContent='Reach out to Our Amazing Team'
//             contentList.innerHTML='<li>This may not be able to be an unordered list</li>'
         
//             break;
        
//         default:
//             title.textContent = 'Code Platoon';
//             subTitle.textContent = '(bootleg)';
//             contentList.innerHTML = '<li>This is not the official Code Platoon WebPage</li><li>None of the information here</li><li>Corresponds to actual personal data</li>';
          

//     }
// }








/*
// https://www.codeplatoon.org/wp-content/uploads/2022/04/CN_100_Award_Badge.png
// https://www.codeplatoon.org/wp-content/uploads/2023/02/Candid2023.png
https://www.codeplatoon.org/wp-content/uploads/2021/05/Mil_Spouses_in_Tech.jpeg.jpg

https://www.codeplatoon.org/wp-content/uploads/2018/08/now-offering-python-for-2019-sessions.jpg

https://www.codeplatoon.org/wp-content/uploads/2018/08/testimonials-bg.jpg

https://www.codeplatoon.org/wp-content/uploads/2020/11/working.jpg
*/