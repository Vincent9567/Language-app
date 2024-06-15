import { useState, useEffect } from "react";
import './sideBar.css'

import NavButton from "./NavButton";

function SideBar() {
    return (  
        <>
            <div className="sideBar-container">
                <div className="header">
                    <h2 className="title">LANGUAGE APP</h2>
                </div>
                <div className="buttonContainer">
                    <NavButton 
                    name="Home"
                    icon='Home'
                    link='/home'/> 
                    <NavButton 
                    name="Create Flashcards"
                    icon='duplicate-outline'
                    link='/createcard'/>  
                    <NavButton 
                    name="Study Flashcards"
                    icon='book'
                    link='/studycards'/>  
                    <NavButton 
                    name="Account"
                    icon='accessibility-outline'
                    link='/home'/>  
                    <NavButton 
                    name="Help"
                    icon='help-circle-outline'
                    link='/home'/>  
                </div>
                <div className="cardCountContainer">
                    <h4>New Flashcards</h4>
                    <h4>Repeat Flashcards</h4>
                </div>
            </div>
        </>
    );
}

export default SideBar;