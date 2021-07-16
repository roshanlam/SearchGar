import React, {
  FC,
  ChangeEvent,
  FocusEvent,
  ButtonHTMLAttributes,
  InputHTMLAttributes,
} from "react";

export const FormCard: FC = ({ children }) => (
  <div className="bg-white shadow-md p-8 lg:p-10 xl:p-12 lg:w-3/6 xl:w-2/6 items-center flex flex-col w-96 space-y-4 > *">
    {children}
  </div>
);

export const FormInput: FC<
  InputHTMLAttributes<any> & {
    label?: string;
  }
> = ({
  disabled,
  label,
  name,
  onBlur,
  onChange,
  placeholder,
  required,
  type,
  value,
}) => (
  <div className="w-full">
    {label ? <label htmlFor={name}>{label}</label> : null}
    <input
      className="rounded-md border w-full px-2 py-1"
      disabled={disabled}
      name={name}
      onBlur={onBlur}
      onChange={onChange}
      placeholder={placeholder}
      required={required}
      type={type}
      value={value}
    />
  </div>
);

export const FormButton: FC<ButtonHTMLAttributes<any>> = ({
  children,
  ...buttonAttributes
}) => (
  <button
    className="bg-gray-900 w-full text-white rounded-full border-black p-1"
    {...buttonAttributes}
  >
    {children}
  </button>
);