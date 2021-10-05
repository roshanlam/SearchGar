import React, { FC, useMemo } from 'react';
import clsx from 'clsx';
import { Icon, IconType } from '../Icon';
import { bemify } from '../../../utils/bemify';

import './Toast.scss';

export type ToastType = 'success' | 'warning';

export interface ToastProps {
    /** Optional. Extra classNames you can pass. */
    className?: string;
    /** Required. The type for Toast component. */
    type: ToastType;
}

/**
 * Toast component.
 */
const Toast: FC<ToastProps> = ({ children, className, type = 'warning' }) => {
    const iconType = useMemo<IconType>(() => {
        switch (type) {
            case 'success':
                return IconType.thumbsUp;
            default:
                return IconType.alertCircleOutline;
        }
    }, [type]);

    return (
        <div
            className={clsx('Toast', className, {
                [`Toast--${type}`]: true,
                ...bemify(className, `--${type}`),
            })}
            data-testid="Toast"
        >
            <Icon
                className={clsx('Toast__icon', {
                    [`Toast__icon--${type}`]: true,
                    ...bemify(className, '__icon'),
                    ...bemify(className, `__icon--${type}`),
                })}
                icon={iconType}
                size={20}
                dataTestId="Toast__icon"
            />
            <div
                className={clsx('Toast__text', { ...bemify(className, '__text') })}
                data-testid="Toast__text"
            >
                {children}
            </div>
        </div>
    );
};

export default Toast;