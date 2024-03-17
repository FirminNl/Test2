import { Button, LinearProgress, TextField, toggleButtonGroupClasses } from '@mui/material'
import React, { Component } from 'react'
import { default as CharacteristicView } from '../../api/Views/CharacteristicView'
import DescriptionView from '../../api/Views/DescriptionView'
import { default as InfoView } from '../../api/Views/InfoView'
import SelectionView from '../../api/Views/SelectionView'
import { SuccessMessage } from '../constants'
import InfoObject from './InfoObject'
import NewEigenschaftDialog from './NewEigenschaftDialog'
import './Profildaten.css'


export class Eigenschaften extends Component {
  constructor(props) {
    super(props)

      this.state = {
        questionAnswerArray:[],
        success: null,
        openNewEigenschaftDialog: false,
        successMessage: "",
        loading: true
      }
    }

    isAnswerEmpty = () => {
      const isAnswerEmpty = this.state.questionAnswerArray.some(
        (item) => item.notSaved === true
      );
      return isAnswerEmpty
    }

    handleIsSaved = (notSaved, infoID) => {
      const itemIndex = this.state.questionAnswerArray.findIndex(item => item.info.getID() === infoID);
      let newQuestionAnswerArray = this.state.questionAnswerArray
      newQuestionAnswerArray[itemIndex].notSaved=notSaved
      this.setState({
        questionAnswerArray: newQuestionAnswerArray
      })
      const isEmptyString = this.isAnswerEmpty();
      this.props.handleIsSaved(isEmptyString)
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

    closeNewEigenschaftDialog = () =>{
      this.setState({
        openNewEigenschaftDialog: false
      })
    }
    openNewEigenschaftDialog = () =>{
      this.setState({
        openNewEigenschaftDialog: true
      })
    }
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
                  { answer: answer, question: question[0], info: info, notSaved: false},
                ];
                newQuestionAnswerArray.sort((a, b) =>  a.question.id - b.question.id);
                return {
                  questionAnswerArray: newQuestionAnswerArray,
                };
              });
            }
            this.setState({
              loading: false
            })
          })
          .catch((err) => console.log("error", err));
      };

      deleteInfo = (infoObject) => {
        const newQuestionAnswerArray = this.state.questionAnswerArray.filter((item) => item.info.getID() !== infoObject.getID())
        this.setState({
          questionAnswerArray: newQuestionAnswerArray,
          success: true,
          successMessage: "Erfolgreich gelöscht"
        })
      }
    getAllinfoObjects = () => {
      if(this.props.isSearchprofile){
        return new Promise((resolve, reject) => {
            InfoView.getView().getBySearchprofile_id(this.props.profile.getID()).then((inf) => resolve(inf))
            .catch((error) => reject(error))
          })
      }
      else{
        return new Promise((resolve, reject) => {
            InfoView.getView().getByUserprofile_id(this.props.profile.getID()).then((inf) => resolve(inf))
        .catch((error) => reject(error))
        })
      }
      };

    handleSuccessClose = () =>{
        this.setState({success:false})
     }

     saveInfo = (info) =>{
      if(info.getIsSelection()){
        this.getSelectionByID(info)
      }
      else{
        this.getDescriptionByID(info)
      }
      this.closeNewEigenschaftDialog()
     }

    componentDidMount(){
        this.getAnswerObjects();
    }


  render() {
    return (
        <div className='eigenschaften__container'>
        <div className="eigenschaften__header">
            <h2 className="eigenschaften__header-h">Eigenschaften</h2>
            <p className="eigenschaften__header-p">Ergänze bitte deine Eigenschaften!</p>
        </div>
        {this.state.loading ?
        <div style={{marginTop: "1rem", marginBottom:"2rem"}}>
          <LinearProgress/> 
        </div>
        :
        <div className="eigenschaften__content">
            {this.state.questionAnswerArray ?
            this.state.questionAnswerArray.map((item) =>
            <InfoObject  handleIsSaved={this.handleIsSaved} isSearchprofile={this.props.isSearchprofile} key={item.question.getID()} user={this.props.user} answer={item.answer} question={item.question} info={item.info} isSelection={item.question.getIsSelection()} deleteInfo={this.deleteInfo}/>):null}
            <Button sx={{width:"fit-content", marginTop:"2rem"}} variant="contained" onClick={this.openNewEigenschaftDialog}>Eigenschaft hinzufügen</Button>
            <SuccessMessage  successText={this.state.successMessage} open={this.state.success} closeSuccess={this.handleSuccessClose}/>
            <NewEigenschaftDialog  profile={this.props.profile} questionAnswerArray={this.state.questionAnswerArray} isSearchprofile={this.props.isSearchprofile} open={this.state.openNewEigenschaftDialog} onClose={this.closeNewEigenschaftDialog} user={this.props.user} saveInfo={this.saveInfo}/>
        </div>
          }
    </div>
    )
  }
}

export default Eigenschaften