import './createCard.css'


function CreateCard() {
    return (  
        <>
         <div className="createCard-container">
            <div className="input-container">
             <label htmlFor='word-input'>Enter word</label>
             <input type="text" id='word-input'/>
            </div>
            <button className="create-card">Create Flashcard</button>
         </div>
        </>
    );
}

export default CreateCard;