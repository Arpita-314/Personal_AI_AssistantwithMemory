import { useEffect } from 'react';
import MemoryGardenRPG from './MemoryGardenRPG';

// Storage API polyfill for development
if (typeof window !== 'undefined' && !window.storage) {
  window.storage = {
    get: async (key) => {
      const value = localStorage.getItem(key);
      return value ? { value } : null;
    },
    set: async (key, value) => {
      localStorage.setItem(key, value);
      return true;
    },
    remove: async (key) => {
      localStorage.removeItem(key);
      return true;
    }
  };
}

function App() {
  return <MemoryGardenRPG />;
}

export default App;
