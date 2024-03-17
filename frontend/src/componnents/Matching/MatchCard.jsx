import ChatIcon from '@mui/icons-material/Chat';
import InfoIcon from '@mui/icons-material/Info';
import { Button, CircularProgress, IconButton } from "@mui/material";
import React, { Component } from "react";
import ChatBO from '../../api/ChatBO';
import MatchingBO from '../../api/MatchingBO';
import CharacteristicView from '../../api/Views/CharacteristicView';
import ChatView from '../../api/Views/ChatView';
import DescriptionView from '../../api/Views/DescriptionView';
import InfoView from '../../api/Views/InfoView';
import MatchingView from '../../api/Views/MatchingView';
import SelectionView from '../../api/Views/SelectionView';
import SimilarityView from '../../api/Views/SimilarityView';
import UserProfileView from "../../api/Views/UserProfileView";
import ChatDialog from '../ChatDialog';
import { SuccessMessage } from '../constants';
import "./Matching.css";
import ProfileDetailsPopUp from './ProfileDetailsPopUp';

export class MatchCard extends Component {
  constructor(props) {
    super(props)
    this.state = {
      userprofile: null,
      questionAnswerArray:[],
      cardAttributesArray: [],
      similarity: "",
      openProfileDetails: false,
      success: false,
      successMessage: "",
      loading: false,
      openActiveChat: false,
      isUnseen: false,
      testState: false
    }
  }

getUserProfile = () => {
  UserProfileView.getView().getById(this.props.candidateID).then((prof) =>{
    this.setState({
      userprofile: prof[0]
    })
    this.getAnswerObjects();
    if(this.props.parentComponent === "match"){
      this.getSimilarityscore()
    }
  })
  .catch((err) => console.log("error", err));
}

getSimilarityscore = () => {
  SimilarityView.getView().getByMatching_id(this.props.parentObject.getID()).then((sim) => {
    this.setState({
      similarity: sim[0]
    })
  })
  .catch((err) => console.log("error", err));
}
getAnswerObjects = async () => {
  this.getAllinfoObjects()
    const infoObjects = await this.getAllinfoObjects()
    infoObjects.forEach((info) => {
        if(info.getIsSelection()){
            this.getSelectionByID(info)
          }
          else{
            this.getDescriptionByID(info)
        }
    })
  };

  refreshSimilarity = () => {
    this.getSimilarityscore()
    console.log("ZWEITER SCHRITT")
    this.forceUpdate();
  }
  getAllinfoObjects = () => {
      return new Promise((resolve, reject) => {
          InfoView.getView().getByUserprofile_id(this.props.candidateID).then((inf) => resolve(inf))
          .catch((err) => console.log("error", err));
      })

    };

    getSelectionByID = (info) => {
      SelectionView.getView().getById(info.getAnswerId()).then((answ) => {
       this.getQuestionById(answ[0], info)
      })
      .catch((err) => console.log("error", err));
}
getDescriptionByID = (info) => {
      DescriptionView.getView().getById(info.getAnswerId()).then((answ) => this.getQuestionById(answ[0], info))
      .catch((err) => console.log("error", err));
}
getCardAttributes = (questionAnswerArray) => {
  let cardAttributesArray = [];
  questionAnswerArray.forEach((item) =>{
    if(item.question.getID() === 3 || item.question.getID() === 4){
      cardAttributesArray.push(item)
    }
  })
  this.setState({
    cardAttributesArray: cardAttributesArray
  })
}
getQuestionById = (answer, info) => {
  CharacteristicView.getView()
    .getById(answer.getCharacteristicId())
    .then((question) => {
      const isAnswerPresent = this.state.questionAnswerArray.some(
        (item) => item.info.getID() === info.getID()
      );
      if (!isAnswerPresent) {
        this.setState((prevState) => {
          const newQuestionAnswerArray = [
            ...prevState.questionAnswerArray,
            { answer: answer, question: question[0], info: info },
          ];
          newQuestionAnswerArray.sort((a, b) =>  a.question.id - b.question.id);
          this.getCardAttributes(newQuestionAnswerArray)
          return {
            questionAnswerArray: newQuestionAnswerArray,
          };
        });
      }
    })
    .catch((err) => console.log("error", err));
};

openProfileDetails = () => {
  this.setState({
    openProfileDetails: true
  })
  if(this.props.parentComponent==="match"){
    this.unseenMatch()
  }
}

unseenMatch = () => {
  let newMatchingObject = Object.assign(this.props.parentObject, MatchingBO)
  newMatchingObject.setUnseenProfile(false)
  MatchingView.getView().update(newMatchingObject).then((match)=>{
  })
  .catch((err) => console.log("error", err));
}

closeProfileDetails = () => {
  this.setState({
    openProfileDetails: false
  })
}
openActiveChat = () => {
  this.setState({
    openActiveChat: true
  })
}
closeActiveChat = () => {
  this.setState({
    openActiveChat: false
  })
}

removeEntry = (entry, successMessage) => {
  this.setState({
    success: true,
    successMessage: successMessage
  })
  this.props.removeEntry(entry)
};

closeSuccess = () => {
  this.setState({
    success: false
  })
}

componentDidMount(){
  this.getUserProfile()
}

  render() {
    return (
      <>
      {this.state.userprofile ?
      <div className="card-wrapper"
      style={{
        backgroundColor: this.props.parentComponent === "match" ? "rgb(108, 181, 255, 31%)":
        this.props.parentComponent === "gesendeteAnfrage" ?
        "#F1D3FF":
        this.props.parentComponent === "empfangeneAnfrage" ?
        "#F1D3FF":
        this.props.parentComponent === "activeChats" ?
        "#D3FFDF":
        this.props.parentComponent === "blocked" ?
        "#FFD3D3":
        this.props.parentComponent === "marked" ?
        "#FFFBD3":null,

      }} >
        <div className="card-right-side" >
        <div className="card-attr" >
        <h2 className="card-attr-name" >
          Name
        </h2>
          <p className="card-attr-value">{this.state.userprofile.getFirstname()} {this.state.userprofile.getSurname()}</p>
        </div>
          {
            this.state.cardAttributesArray.length > 0 ?
          this.state.cardAttributesArray.map((item)=>
          <div className="card-attr"  key={item.question.getID()}>
        <h2 className="card-attr-name">{item.question.getName()}</h2>
          <p className="card-attr-value">{item.answer.getAnswer()}</p>
        </div>
          )
        :
        <div style={{display: "flex", flexDirection:"column", gap: "1rem"}}>
        <CircularProgress/>
        <CircularProgress/>
        </div>
        }
        </div>
        <div className="card-left-side">
            {this.props.parentComponent === "match"?
          <div>
            <h2 className="card-score">Matching-Score</h2>
            {this.state.similarity ?
              <h2 className="card-score-value">
              {this.state.similarity.getScore()}%
              </h2> : <CircularProgress/>}
          </div>
                :
                this.props.parentComponent === "activeChats"?
                <IconButton onClick={this.openActiveChat}>
                  <ChatIcon sx={{fontSize:"3rem"}}/>
                </IconButton>
              :null}
            <Button sx={{mb:2}} onClick={this.openProfileDetails} variant="contained" startIcon={<InfoIcon/>}>Mehr erfahren</Button>
        </div>
      </div>
        :
        <div className='loading-card'>
        <CircularProgress/>
        </div>
        }
          <ProfileDetailsPopUp open={this.state.openProfileDetails}
          parentComponent={this.props.parentComponent}
          user={this.props.user}
          candidate={this.state.userprofile}
          candidateID={this.props.candidateID}
          handleClose={this.closeProfileDetails}
          removeEntry={this.removeEntry}
          questionAnswerArray={this.state.questionAnswerArray}
          parentObject={this.props.parentObject}
           />
          {
            this.props.parentComponent === "activeChats" ?
            <ChatDialog open={this.state.openActiveChat} handleClose={this.closeActiveChat} chat={this.props.parentObject} candidate={this.state.userprofile} user={this.props.user}/>
            :null
          }
      </>
    );
  }
}

export default MatchCard;
