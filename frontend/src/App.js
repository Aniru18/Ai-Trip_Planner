
import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from "react-markdown";
import { Send, Globe, Sparkles, Bot, User } from 'lucide-react';
import './App.css';

const BASE_URL = "http://localhost:8000";

function App() {
  const [userInput, setUserInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!userInput.trim()) return;

    const userMessage = {
      type: 'user',
      content: userInput,
      timestamp: new Date().toLocaleTimeString()
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const response = await axios.post(`${BASE_URL}/query`, {
        question: userInput
      });

      if (response.status === 200) {
        const botMessage = {
          type: 'bot',
          content: response.data.answer || "No answer returned.",
          timestamp: new Date().toLocaleTimeString()
        };
        setMessages(prev => [...prev, botMessage]);
      } else {
        throw new Error('Failed to get response');
      }
    } catch (error) {
      const errorMessage = {
        type: 'bot',
        content: "Sorry, I couldn't process your request. Please try again.",
        timestamp: new Date().toLocaleTimeString(),
        isError: true
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
      setUserInput('');
    }
  };

  return (
    <div className="app">
      <div className="container">
        <div className="header">
          <div className="header-content">
            <Globe className="header-icon" size={32} />
            <h1>AI Travel Planner</h1>
            <p className="subtitle">Your intelligent travel companion</p>
          </div>
        </div>

        <div className="chat-container">
          {messages.length === 0 ? (
            <div className="welcome-section">
              <div className="welcome-card">
                <Sparkles className="welcome-icon" size={48} />
                <h2>Welcome to your AI Travel Assistant!</h2>
                <p>I can help you plan amazing trips. Just tell me where you want to go!</p>
              </div>
            </div>
          ) : (
            <div className="messages">
              {messages.map((message, index) => (
                <div key={index} className={`message ${message.type}`}>
                  <div className="message-avatar">
                    {message.type === 'user' ? <User size={20} /> : <Bot size={20} />}
                  </div>
                  <div className="message-content">
                    <div className={`message-bubble ${message.isError ? 'error' : ''}`}>
                      {message.type === 'bot' && !message.isError ? (
                        <ReactMarkdown>{message.content}</ReactMarkdown>
                      ) : (
                        <p>{message.content}</p>
                      )}
                    </div>
                  </div>
                </div>
              ))}
              {isLoading && (
                <div className="message bot">
                  <div className="message-avatar">
                    <Bot size={20} />
                  </div>
                  <div className="message-content">
                    <div className="loading-bubble">
                      <p>Planning your perfect trip...</p>
                    </div>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>

        <form onSubmit={handleSubmit} className="input-form">
          <div className="input-container">
            <input
              type="text"
              value={userInput}
              onChange={(e) => setUserInput(e.target.value)}
              placeholder="e.g., Plan a trip to Goa for 5 days"
              className="input-field"
              disabled={isLoading}
            />
            <button type="submit" className="send-button" disabled={isLoading || !userInput.trim()}>
              <Send size={20} />
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default App;
