import * as React from 'react';
import { Meta, Story } from '@storybook/react';

import { Icon, IconProps, IconType } from './index';
import '../../styles/colors.css';
import './IconStories.scss';

const meta: Meta = {
    title: 'Icon',
    component: Icon as any,
    argTypes: {
        className: {
            defaultValue: 'primary gray-100-bg',
        },
        icon: {
            control: {
                type: 'select',
                options: IconType,
            },
            defaultValue: IconType.alert,
        },
    },
    parameters: {
        controls: { expanded: true },
    },
};

export default meta;

const Template: Story<IconProps> = props => <Icon {...props} />;

// By passing using the Args format for exported stories, you can control the props for a component for reuse in a test
// https://storybook.js.org/docs/react/workflows/unit-testing
export const WithoutOnClick = Template.bind({});
WithoutOnClick.args = {
    onClick: undefined,
    onKeyDown: undefined,
};

export const WithOnClick = Template.bind({});
WithOnClick.args = {
    onClick() {
        alert('You pressed me.');
    },
    onKeyDown(e?: React.KeyboardEvent<HTMLDivElement>) {
        alert(`You pressed ${e?.key}`);
    },
};