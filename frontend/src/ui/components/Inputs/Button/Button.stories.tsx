import * as React from 'react';
import { Meta, Story } from '@storybook/react';

import {
    Button,
    ButtonColor,
    ButtonProps,
    ButtonType,
    ButtonVariant,
} from './index';

const meta: Meta = {
    title: 'Button',
    component: Button,
    argTypes: {
        children: {
            control: 'text',
            defaultValue: 'Click me!',
        },
        color: {
            control: {
                type: 'select',
                options: ButtonColor,
            },
            defaultValue: ButtonColor.primary,
        },
        type: {
            control: {
                type: 'select',
                options: ButtonType,
            },
            defaultValue: ButtonType.button,
        },
        variant: {
            control: {
                type: 'select',
                options: ButtonVariant,
            },
            defaultValue: ButtonVariant.contained,
        },
    },
    parameters: {
        controls: { expanded: true },
    },
};

export default meta;

const Template: Story<ButtonProps> = props => <Button {...props} />;

// By passing using the Args format for exported stories, you can control the props for a component for reuse in a test
// https://storybook.js.org/docs/react/workflows/unit-testing
export const Default = Template.bind({});
Default.args = {
    onClick() {
        alert('You pressed me.');
    },
};