// refactor App.js to use Context instead of prop drilling to pass the imageSize prop

import { createContext } from "react";

export const ImageSizeContext = createContext(100); // default value is 100