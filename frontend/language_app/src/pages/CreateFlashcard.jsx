import CreateCard from '../components/CreateCard';
import SideBar from '../components/SideBar';
import './createFlashcard.css'



function CreateFlashCard() {
    return (  
        <>
        <div className="parent-container">
            <div className="sidebar">
                <SideBar className='sidebar' />
            </div>

            <div className="createCard-Container">
                <CreateCard className='createCard-Container'/>
            </div>
        </div>
        </>
    );
}

export default CreateFlashCard;