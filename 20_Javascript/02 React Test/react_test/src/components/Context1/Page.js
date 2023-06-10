import Heading from './Heading.js';
import Section from './Section.js';

// https://beta.reactjs.org/learn/passing-data-deeply-with-context#using-and-providing-context-from-the-same-component

// everytime you create a new <Section> component, Heading gets 1 size smaller

export default function Page() {
  return (
    <Section>
      <Heading>Title</Heading>
      <Section>
        <Heading>Heading</Heading>
        <Heading>Heading</Heading>
        <Section>
          <Heading>Sub-heading</Heading>
          <Heading>Sub-heading</Heading>
          <Section>
            <Heading>Sub-sub-heading</Heading>
            <Heading>Sub-sub-heading</Heading>
          </Section>
        </Section>
      </Section>
    </Section>
  );
}
