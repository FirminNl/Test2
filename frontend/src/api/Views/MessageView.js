import API from "../API";
import MessageBO from "../MessageBO";
export default class MessageView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new MessageView();
    }
    return this.#view;
  }
  #getByidURL = (id) => `message/${id}`;
  #getByChatIdURL = (chatId) => `message_from_chat/${chatId}`;
  #createURL = () => `message`;
  #updateURL = (id) => `message/${id}`;
  #deleteURL = (id) => `message/${id}`;

  getByid(id) {
    return API.getAPI().get(this.#getByidURL(id), MessageBO);
  }

  getByChatId(chatId) {
    return API.getAPI().get(this.#getByChatIdURL(chatId), MessageBO);
  }

  create(message) {
    return API.getAPI().create(this.#createURL(), message, MessageBO);
  }

  update(message) {
    return API.getAPI().update(
      this.#updateURL(message.getID()),
      message,
      MessageBO
    );
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), MessageBO);
  }
}
