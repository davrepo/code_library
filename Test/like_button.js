'use strict';

function LikeButton(props) {
  const [liked, setLiked] = React.useState(false);

  if (liked) {
    return 'You liked comment number ' + props.commentID;
  }

  return React.createElement(
    'button',
    { onClick: () => setLiked(true) },
    'Like'
  );
}

// Find all DOM containers, and render Like buttons into them.
// Note we're using CSS classes instead of IDs so that we can find several nodes.
document.querySelectorAll('.like-button-root').forEach((rootNode) => {
  const root = ReactDOM.createRoot(rootNode);
  // Read the comment ID from a data-* attribute.
  const commentID = parseInt(rootNode.dataset.commentid, 10);
  root.render(
    React.createElement(LikeButton, { commentID: commentID })
  );
});