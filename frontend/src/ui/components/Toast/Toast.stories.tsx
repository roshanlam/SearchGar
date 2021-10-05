import * as React from 'react';
import { Meta, Story } from '@storybook/react';

import Toast, { ToastProps } from './index';
import '../../styles/core.css';
import '../../styles/colors.css';
import './Toast.scss';

const meta: Meta = {
    title: 'Toast',
    component: Toast,
    argTypes: {},
    parameters: {
        controls: { expanded: true },
    },
};

export default meta;

const Template: Story<ToastProps> = props => (
    <Toast {...props}>Example Toast</Toast>
);

// By passing using the Args format for exported stories, you can control the props for a component for reuse in a test
// https://storybook.js.org/docs/react/workflows/unit-testing
export const ToastStory = Template.bind({});