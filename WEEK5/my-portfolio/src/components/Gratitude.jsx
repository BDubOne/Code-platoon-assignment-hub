
import Carousel from 'react-bootstrap/Carousel';


function Gratitude({ userProfiles} ) {


    return (
      <>
     
        <main>
             <h3>
                Organizations
            </h3>
            <Carousel>
                <Carousel.Item>
                    <a href="https://www.codeplatoon.org">
                        <img
                        className="d-block w-100"
                        src="https://www.codeplatoon.org/wp-content/uploads/2018/10/CP-Logo-White-NoPadding.png"
                        alt="code-platoon logo"
                        />
                    </a>
                    <Carousel.Caption id="gratitudecaption">
                        <h3>Code Platoon</h3>
                        <p>Code Platoon is a fantastic organization for any military-afiliated person who wishes to delve into software development. Francisco Avila and Adam Cahan have put together a fantastic curriculum, supported by an amazing staff and wonderful TAs (Shoutout to Dakota, Tristan, Polina and Shengan!)  </p>
                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <a href="https://www.codeplatoon.org">
                        <img
                        className="d-block w-100"
                        src="https://www.codeplatoon.org/wp-content/uploads/2018/10/CP-Logo-White-NoPadding.png"
                        alt="code-platoon logo"
                        />
                    </a>
                    <Carousel.Caption id="gratitudecaption">
                        <h3>Code Platoon</h3>
                        <p>Code Platoon is a fantastic organization for any military-afiliated person who wishes to delve into software development. Francisco Avila and Adam Cahan have put together a fantastic curriculum, supported by an amazing staff and wonderful TAs (Shoutout to Dakota, Tristan, Polina and Shengan!)  </p>
                    </Carousel.Caption>
                </Carousel.Item>
            
            </Carousel>
             <h3>
            People
        </h3>
        <Carousel>
            {userProfiles.map(profile => (
            <Carousel.Item key="{profile.id}">
                <a href={profile.html_url} target="_blank" rel="noopener noreferrer">
                    <img 
                    className="d-block w-100"
                    src={profile.avatar_url}
                    alt={profile.name}
                    />
                    <Carousel.Caption>
                        <h3>{profile.name}</h3>
                        <p>{profile.bio}</p>
                    </Carousel.Caption>
                </a>
            </Carousel.Item>
            ))}
        </Carousel>       


        </main>
       

    </>
    )
}

export default Gratitude