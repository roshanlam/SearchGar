import React, {FC, ReactNode, useState} from 'react';
import {useSelector} from 'react-redux';
import {Link} from 'react-router-dom';
import clsx from 'clsx';

import {A, Icon, IconType} from 'components';
import './TopNavMobileMenu.scss';

interface ComponentProps {
  closeMenu(): void;
  menuOpen: boolean;
  smallDevice: boolean;
  toggleMenu(): void;
}

const TopNavMobileMenu: FC<ComponentProps> = ({closeMenu, menuOpen, smallDevice, toggleMenu}) => {
  const [openSection, setOpenSection] = useState<'getStarted' | 'more' | 'other' | null>(null);

  const handleColumnTitleClick = (section:  'getStarted' | 'more' | 'other') => (): void => {
    if (!smallDevice) return;
    setOpenSection(openSection === section ? null : section);
  };

  const renderColumn = (
    section: 'getStarted' | 'more' | 'other',
    title: string,
    links: ReactNode,
  ): ReactNode => {
    return (
      <div className="TopNavMobileMenu__column">
        <button className="TopNavMobileMenu__title-wrapper" onClick={handleColumnTitleClick(section)}>
          <span className="TopNavMobileMenu__column-title TopNavMobileMenu__column-title--accordion">{title}</span>
          {smallDevice && (
            <span className="TopNavMobileMenu__icon-holder">
              <Icon
                className={clsx('TopNavMobileMenu__chevron-icon', {
                  'TopNavMobileMenu__chevron-icon--open': openSection === section,
                })}
                icon={IconType.chevronDown}
              />
            </span>
          )}
        </button>

        {(!smallDevice || openSection === section) && <div className="TopNavMobileMenu__links">{links}</div>}
      </div>
    );
  };

  const renderOtherSmallDeviceLink = (title: string, to: string): ReactNode => (
    <div className="TopNavMobileMenu__column TopNavMobileMenu__not-visible-tab">
      <Link to={to}>
        <button className="TopNavMobileMenu__column-title">{title}</button>
      </Link>
    </div>
  );

  const renderOtherSmallDeviceLinks = (): ReactNode => (
    <>
      <div className="TopNavMobileMenu__separator TopNavMobileMenu__not-visible-tab" />
      {renderOtherSmallDeviceLink('Resource Center', '/rc')}
      {renderOtherSmallDeviceLink('', '')}
    </>
  );

  const renderMenu = (): ReactNode => {
    return (
      <>
        <div className="TopNavMobileMenu__dropdown-container">
          {renderColumn(
            'getStarted',
            'Get Started',
            <>
              {renderMobileLink('Something', 'Something')}
              {renderMobileLink('Assignments', '/assignments')}
            </>,
          )}
          {renderColumn(
            'more',
            'More',
            <>
              {renderMobileLink('Quiz', '/quiz')}
            </>,
          )}
          {smallDevice
            ? renderOtherSmallDeviceLinks()
            : renderColumn(
                'other',
                'Other',
                <>
                  {renderMobileLink('Something Else', '/')}
                </>,
              )}
        </div>
        <div className={clsx('TopNavMobileMenu__overlay')} onClick={closeMenu} role="button" tabIndex={0} />
      </>
    );
  };

  const renderMobileLink = (label: string, to: string, isExternal?: boolean): ReactNode => {
    if (isExternal) {
      return (
        <A className="TopNavMobileMenu__link" href={to} newWindow={false}>
          {label}
        </A>
      );
    }
    return (
      <Link className="TopNavMobileMenu__link" to={to}>
        {label}
      </Link>
    );
  };

  return (
    <div className="TopNavMobileMenu">
      <button className="TopNavMobileMenu__button" onClick={toggleMenu}>
        <Icon icon={IconType.menu} size={24} />
      </button>
      {menuOpen && renderMenu()}
    </div>
  );
};

export default TopNavMobileMenu;
