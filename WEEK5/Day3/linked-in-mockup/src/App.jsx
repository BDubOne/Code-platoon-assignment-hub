import { useState } from 'react'

import './App.css'

function App() {


  return (
    <>
    <header id="header">
      <nav id="headnav1">
        <a className='navitems'id="logo-btn" href="#personal-feed"><img src="#" alternatetext="LI"/></a>
        <input className ='navitems' id="search-li-btn" type="search" placeholder="search"/>
        <div className="navitems">
        <a id="home-btn" href="#home"><img src="#" alternatetext="home"/>Home</a>
        </div>
        <div className="navitems">
        <a id="my-network-btn" href="#my-network"><img src="#" alternatetext="network"/>My Network</a>
        </div>
        <div className="navitems">
        <a id="jobs-btn" href="#jobs"><img src="#" alternatetext="jobs"/>Jobs</a>
        </div>
        <div className="navitems">
        <a id="messaging-btn" href="#messaging"><img src="#" alternatetext="messaging"/>Messaging</a>
        </div>
        <div className="navitems">
        <a id="notifications-btn" href="#notifications"><img src="#" alternatetext="notifications"/>Notifications</a>
       </div>
       <div className="navitems">
       <img src="#" alternatetext="mee-menu"/>
        <input id="me-menu" type="menu"/>
        </div>
        <div className="navitems">
          <img src="#" alternatetext="businessmenu"/>
        <input id="business-menu" type="menu"/>
        </div>
        <a className="navitems"id="get-hired" href="#premium">Get hired faster. Try Premium Free</a>
      </nav>
      <nav id="headnav2">
        <img className="navitems" id="profileicon" src="#" alternatetext="profileicon"/>
        <div id="navintro" className="navitems">
          <div id="name-gender">
          <h3 className="name">Bryan Bartell</h3>
          <p className="gender">(He/Him)</p>
          </div>
          <br/>
          <div className="jobs">
          <p>Full-stack Software Developer, Project Management Specialist, Data Analyst</p>
          </div>
        </div>
        <button className="navitems">More</button>
        <button className="navitems">Add profile Section</button>
        <button className="navitems">Open to</button>
      </nav>
    </header>

    <main>
      <div id="left-side">
        <div id="left-head">
          <nav id="left-nav">
            <a id="profile-viewers" href="#">1000 profile viewers</a>
            <p>Past 90 days</p>
            <a id="analytics" href="#">View all analytics ---</a>
          </nav>
          <div id="left-head-imgs">
          <img id="banner" src="#" placeholder="banner image"/>
          <img id="profile-button" src="#" placeholder="profile-button"/>
          </div>
          <div id="bizcard">
            <div id="biztext">
              <h2 className="name">Bryan Bartell</h2>
              <p className="gender">(He/Him)</p>
              <br/>
              <p className="jobs">Full-stack Software Developer, Project Management Specialist, Data Analyst</p>
              <p className="grey"id="address">Splendora, Texas, United States -</p>
              <a id="contact" href="#">Contact</a>
              <br/>
              <br/>
              <br/>
              <a className="name" href="#">1000 Connections</a>
              <br/>
              
              <ul className="inline">
                <button>Open to</button>
                <button>Add profile section</button>
                <button>More</button>
              </ul>
              <marquee className="inline">
                <div className="carousel-item">
                  Open to work
                </div>
                <div className="carousel-item">
                  Showcase Services
                </div>
              </marquee>
  
            </div>
            <div id="schools">
            <a id="edit" href="#"><img src="#"/></a>
            <a className="school" href="https://www.codeplatoon.org/"><img src="#" alternatetext="code-platoon logo"/></a>
            <a className="school" href="#"><img src="#" alternatetext="Kuyper college logo"/></a>

            </div>
            
          </div>
        </div>
        <div className="leftbox">
        <div className="midbox">

          <h2>
            Suggested for you
          </h2>
          <img className ="floatleft" src="#" alternatetext="eye-icon"/>
          <p className="grey">Private for you</p>

        </div>
        <div className="leftbox">
          <img className="floatleft" src="#" alternatetext="folder-icon"/>
          <h3>Add Github projects that showcase your skills</h3>
          <p>Show recruiters how you put your skills to use by adding projects to your profile</p>
          <button> Add project</button>
          </div>

        </div>
        <div className="leftbox">
          <div>
          <h2>Resources</h2>
          <img className ="floatleft" src="#" alternatetext="eye-icon"/>
          <p className="grey">Private for you</p>
          </div>
          <div id="creation" className="inline">
            <img src="#"/>
            <h3>Creator Mode</h3>
            <button>Off</button>
          </div>
          <p></p>
            <div id="my-network" className="inline">
              <img src="#"/>
              <h3>My network</h3>
              <button>Off</button>

             </div>

        </div>

      </div>
      <div id="right-side">
        <div className="rightbox">
          <h2> primary Language</h2>
          <p className="grey">English</p>
          <h2>Public Profile & Url</h2>
          <a href="www.linkedin.com/in/bryan-bartell-1657b646">www.linkedin.com/in/bryan-bartell-1657b646</a>

        </div>

      </div>

    </main>
   
  
  
            
          
  



    </>
  )
}

export default App
