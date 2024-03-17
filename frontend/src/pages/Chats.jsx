import React, { Component } from 'react';
import ChatView from '../api/Views/ChatView';
import MatchCard from '../componnents/Matching/MatchCard';

class Chats extends Component {
    constructor(props) {
      super(props)
    
      this.state = {
         chatList: []
      }
    }

    getActiveChats = () => {
        ChatView.getView().getByActiveChat(this.props.user.getID()).then((chats) => {
            this.setState({
                chatList: chats
            })
        })
        .catch((err) => console.log("error", err));
    }

    removeEntry = (entry) => {
        this.setState({
            chatList: this.state.chatList.filter((item) => item.getID() !== entry.getID())
        })
    }

    componentDidMount = () => {
        this.getActiveChats()
    }
    render() {
        return (
            <div className='section-wrapper'>
                <div>
                    <h2 style={{color: "#E41036", margin:0}}>Chats</h2>
                    <p>Hier siehst du deine Chats, wenn eine Kontaktanfrage angenommen wurde!</p>
                </div>
                <div className='section-card-grid'>

                    {this.state.chatList.map((chat) => 

                <MatchCard parentComponent="activeChats" key={chat.getID()} user={this.props.user}
                 candidateID={this.props.user.getID() === chat.getSenderId() ? chat.getReceiverId() : chat.getSenderId()}
                 parentObject={chat}
                 removeEntry={this.removeEntry}/>
                    )}
                </div>
            </div>
        );
    }
}

export default Chats;