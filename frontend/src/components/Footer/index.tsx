import React, {FC, memo} from 'react';
import clsx from 'clsx';
//import SocialMediaIcon from 'components/SocialMediaIcon';
//import {SocialMedia} from 'types/social-media';
//import FooterNavList from './FooterNavList';
import './Footer.scss';

interface ComponentProps {
  className?: string;
}
/*
const navLists = []
*/
const Footer: FC<ComponentProps> = ({className}) => {
  /*
  const renderNavLists = () =>
    navLists.map((list) => <FooterNavList header={list.header} key={list.header} links={list.links} />);
  */
  return (
    <footer className={clsx('Footer', className)} data-testid="Footer">
      <div className="Footer__left">
          {/* <div className="Footer__social-media-links">{renderSocialMediaLinks()}</div> */}
      </div>
    </footer>
  );
};

export default memo(Footer);
