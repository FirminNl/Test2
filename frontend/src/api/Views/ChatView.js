import API from "../API";
import ChatBO from "../ChatBO";
export default class ChatView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new ChatView();
    }
    return this.#view;
  }
  #getByidURL = (id) => `chat/${id}`;
  #getByInvitationURL = (userprofile_id) => `chat_invitation/${userprofile_id}`;
  #getBySentInvitationURL = (userprofile_id) => `chat_sent_invitation/${userprofile_id}`;
  #getByActiveChatURL = (userprofile_id) => `chat_active/${userprofile_id}`;
  #createURL = () => `chat`;
  #updateURL = (id) => `chat/${id}`;
  #deleteURL = (id) => `chat/${id}`;

  getByid(id) {
    return API.getAPI().get(this.#getByidURL(id), ChatBO);
  }

  getByInvitation(userprofile_id) {
    return API.getAPI().get(this.#getByInvitationURL(userprofile_id), ChatBO);
  }

  getBySentInvitation(userprofile_id) {
    return API.getAPI().get(this.#getBySentInvitationURL(userprofile_id), ChatBO);
  }

  getByActiveChat(userprofile_id) {
    return API.getAPI().get(this.#getByActiveChatURL(userprofile_id), ChatBO);
  }

  create(chat) {
    return API.getAPI().create(this.#createURL(), chat, ChatBO);
  }

  update(chat) {
    return API.getAPI().update(
      this.#updateURL(chat.getID()),
      chat,
      ChatBO
    );
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), ChatBO);
  }
}
