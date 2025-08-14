export interface Message {
  sender: string;
  content: string;
  timestamp: string;
}

export interface Agent {
  name: string;
  messagesCount: number;
  lastActive?: string;
}
