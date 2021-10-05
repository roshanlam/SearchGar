import * as React from 'react';
import { Meta, Story } from '@storybook/react';

import { TextField, TextFieldProps, TextFieldType } from './index';
import './TextField.scss';

const meta: Meta = {
    title: 'TextField',
    component: TextField,
    argTypes: {
        type: {
            control: {
                type: 'select',
                options: TextFieldType,
            },
        },
    },
    parameters: {
        controls: { expanded: true },
    },
};

export default meta;

const Template: Story<TextFieldProps> = props => <TextField {...props} />;

// By passing using the Args format for exported stories, you can control the props for a component for reuse in a test
// https://storybook.js.org/docs/react/workflows/unit-testing
export const Default = Template.bind({});
Default.args = {};