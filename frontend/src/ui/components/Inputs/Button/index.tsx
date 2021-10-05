import React, { HTMLAttributes, ReactNode, useEffect, useRef } from 'react';
import clsx from 'clsx';
import { bemify } from '../../../../utils/bemify';

import '../../../styles/colors.css';
import '../../../styles/font.css';
import './Button.scss';

export enum ButtonColor {
    primary = 'primary',
    secondary = 'secondary',
    tertiary = 'tertiary',
}

export enum ButtonType {
    button = 'button',
    reset = 'reset',
    submit = 'submit',
}

export enum ButtonVariant {
    contained = 'contained',
    link = 'link',
}

export interface ButtonProps extends HTMLAttributes<HTMLButtonElement> {
    /** Required. The content of the button. */
    children: ReactNode;
    /** Optional. Extra classNames you can pass. */
    className?: string;
    /** Optional. Determines the color of the button. */
    color?: ButtonColor;
    /** Optional. Disables the button. */
    disabled?: boolean;
    /** Optional. Determines if button is focused. */
    focused?: boolean;
    /** Optional. Adds an onClick event handler to the button. */
    onClick?(e: React.MouseEvent<HTMLButtonElement, MouseEvent>): void;
    /** Optional. Button type. */
    type?: ButtonType;
    /** Optional. Determines the UI of the button. */
    variant?: ButtonVariant;
}

/**
 * Button component.
 */
const Button = function({
                            children,
                            color = ButtonColor.primary,
                            className,
                            disabled = false,
                            focused = false,
                            onClick,
                            type = ButtonType.button,
                            variant = ButtonVariant.contained,
                        }: ButtonProps) {
    const buttonRef = useRef<HTMLButtonElement>(null);

    useEffect(() => {
        if (!disabled && focused) {
            buttonRef.current?.focus();
        }
    }, [disabled, focused, buttonRef]);

    return (
        <button
            className={clsx(
                'Button',
                `Button--${variant}`,
                `Button--${color}`,
                className,
                {
                    'Button--disabled': disabled,
                    ...bemify(className, `--${variant}`),
                    ...bemify(className, `--${color}`),
                    ...bemify(className, '--disabled', disabled),
                }
            )}
            data-testid="Button"
            disabled={disabled}
            onClick={onClick}
            ref={buttonRef}
            tabIndex={disabled ? undefined : 0}
            type={type}
        >
            {children}
        </button>
    );
};

export { Button };