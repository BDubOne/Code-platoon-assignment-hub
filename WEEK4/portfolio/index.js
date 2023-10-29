//Here, we are defining the elements of the static page
function updateContent(navItem, eventType) {
    const title = document.getElementById('title');
    const subTitle = document.getElementById('sub-title');
    const pageContent = document.getElementById('content');

//here, we are creating switchcases for the navbar so that the display can change on hover
    if (eventType === 'hover') {
        switch (navItem) {
            case 'about':

                title.textContent = 'About Me';
                subTitle.textContent = 'Mission Statement';
                pageContent.innerHTML = `
                <p>
                    In a rapidly evolving digital landscape, I am committed to harnessing the power of technology to enhance human well-being and promote lifelong learning. Drawing from diverse experiences in theology, arts, and holistic healing, I aim to create innovative software solutions that celebrate the intersection of language, mathematics, and art. By leveraging coding as a universal language, I aspire to build bridges among diverse communities, ensuring that technology enriches the human experience, rather than compromising it.
                </p>
                `;
                break;
                
                case 'portfolio':
                    title.textContent = 'Portfolio';
                    subTitle.textContent = "Recent Projects";
                    let portfolioHTML = `
                    <table class="portfolio-table">
                        <tr>
                            <td>
                                <a href="link-to-project-1">
                                    <img src="screenshot-of-to-do-list.jpg" alt="project 1">
                                </a>
                            </td>
                            <td>
                                <a href="link-to-project-2">
                                    <img src="screenshot-of-guessing-game.jpg" alt="project 2">
                                </a>
                            </td>
                            <td>
                                <a href="link-to-project-3">
                                    <img src="screenshot-of-guessing-game.jpg" alt="project 3">
                                </a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <a href="link-to-project-4">
                                    <img src="screenshot-of-guessing-game.jpg" alt="project 4">
                                </a>
                            </td>
                            <td>
                                <a href="link-to-project-5">
                                    <img src="screenshot-of-guessing-game.jpg" alt="project 5">
                                </a>
                            </td>
                            <td>
                            <a href="link-to-project-6">
                                <img src="screenshot-of-guessing-game.jpg" alt="project 6">
                            </a>
                            </td>
                        </tr>
                    </table>
                    `
                    pageContent.innerHTML = portfolioHTML;
                    break;

                case 'gratitude':
                    title.textContent = 'Gratitude';
                    subTitle.textContent = "Some of the People and Organizations that Have Made My Journey Possible";
                    pageContent.innerHTML = "<p>Here I will place a table with images tagged to websites, bios and repos</p>";
                    break;

                
                    case 'contact':
                        title.textContent = 'Reach Out';
                        subTitle.textContent = "Here's how you can get in contact with me";
                        pageContent.innerHTML = "<p>Here I will place a table with linked-in and github. On click, they will navigate to a direct email-form (that collects their name and email)</p>";
                        break;

            
            default:
                title.textContent = 'Bryan Bartell';
                subTitle.textContent = 'Junior Fullstack Developer(JS, Python, SQL)';
                pageContent.innerHTML = "<p>Welcome to my homepage! <br>I'd like to take a little time<br>to introduce myself,<br>some of the things I have been working on,<br>and some of the people who have helped me along the way!<br></p>";
            
            

        }
    }
    else if (eventType === 'click') {
        switch(navItem) {
            case 'about':
                title.textContent = 'About Me';
                subTitle.textContent = 'Background and Experience';
                pageContent.innerHTML = `
                <p>About Me
                I am a lifelong student with a natural leadership style that allows me to effortlessly collaborate with teams, fostering a proactive mindset. With diverse experiences in theology, arts, and holistic healing, my passion lies at the intersection of technology and promoting human well-being. Currently enrolled at Code Platoon, I am diving deeper into the realms of Python, Django, SQL, React, and more, ready to apply these skills to foster technological innovation. As a certified Qigong instructor, I incorporate mindfulness in all that I do, ensuring that my solutions are not only effective but also nurture the human spirit. This unique combination of skills makes me an ideal fit for any socially-conscious software company.
                <br>
                <br>
                Let's build tech that truly resonates with human vlues. <a href= "#contact" data-content="contact">Reach out</a> to collaborate!
                </p>
                `;
                break;
        default:
            return;

        }
    }
}
//here we actually listen for the mouse to hover over the given text. By using 'mouseenter', the place that is hovered will remain until another item is hovered
document.addEventListener('DOMContentLoaded', function () {
    const navItems = document.querySelectorAll('.nav a');
    navItems.forEach((navItem) => {
        navItem.addEventListener('mouseenter', () => {
            const dataContent = navItem.getAttribute('data-content');
            updateContent(dataContent, 'hover');
           
        });
        
        navItem.addEventListener('click', (e) => {
            e.preventDefault();
            const dataContent = navItem.getAttribute('data-content');
            updateContent(dataContent, 'click');
        });
    });
});
