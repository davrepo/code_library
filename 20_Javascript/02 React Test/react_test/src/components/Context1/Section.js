import { useContext } from 'react';
import { LevelContext } from './LevelContext.js';

// children is the content of section
export default function Section({ children }) {
    // Section is using the LevelContext, with default value of 0, i.e. level is 0
  const level = useContext(LevelContext);
  return (
    <section className="section">
        {/* level + 1 is the new value of LevelContext */}
        {/* so every time a Section is called, the level is incremented by 1 */}
      <LevelContext.Provider value={level + 1}> 
        {children}
      </LevelContext.Provider>
    </section>
  );
}
