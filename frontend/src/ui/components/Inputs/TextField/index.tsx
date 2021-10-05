import React, { ChangeEvent, FC, FocusEvent, useEffect, useRef } from 'react';
import clsx from 'clsx';
import { bemify } from '../../../../utils/bemify';

import '../../../styles/colors.css';
import '../../../styles/font.css';
import './TextField.scss';

export enum TextFieldType {
    text = 'text',
    number = 'number',
}

export interface TextFieldProps {
    className?: string;
    disabled?: boolean;
    error?: boolean;
    focused?: boolean;
    name?: string;
    onBlur?(e: FocusEvent<HTMLInputElement>): void;
    onChange?(e: ChangeEvent<HTMLInputElement>): void;
    placeholder?: string;
    type?: TextFieldType;
    value?: string;
}

const TextField: FC<TextFieldProps> = ({
                                           className,
                                           disabled = false,
                                           error = false,
                                           focused = false,
                                           name,
                                           onBlur,
                                           onChange,
                                           placeholder = 'Enter',
                                           type = TextFieldType.text,
                                           value,
                                       }) => {
    const inputRef = useRef<HTMLInputElement | null>(null);

    useEffect(() => {
        if (focused && inputRef.current) {
            inputRef.current!.focus();
        }
    }, [focused, inputRef]);

    return (
        <input
            className={clsx('TextField', className, {
                'TextField--error': error,
                ...bemify(className, '--error', error),
            })}
            disabled={disabled}
            name={name}
            onBlur={onBlur}
            onChange={onChange}
            placeholder={placeholder}
            ref={inputRef}
            type={type}
            value={value}
        />
    );
};

export { TextField };