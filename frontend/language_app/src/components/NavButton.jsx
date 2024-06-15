import './navButton.css'
import { useNavigate } from 'react-router-dom';
function NavButton(props) {

    const navigate = useNavigate()

    const handleClick = () => {
        navigate(props.link)
    };

    return (  
        <>  
            <button onClick={handleClick}>
                <ion-icon name={props.icon}></ion-icon><h5 className='buttonTitle'>{props.name}</h5>
            </button> 
        </>
    );
}

export default NavButton;