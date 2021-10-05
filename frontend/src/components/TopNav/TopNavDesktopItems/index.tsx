import React, {useMemo, useState} from 'react';
import {useSelector} from 'react-redux';
import {Link} from 'react-router-dom';

import {Button, IconType} from 'components';
import TopNavLink from 'containers/TopNav/TopNavLink';
import TopNavPopover, {TopNavPopoverItemType} from 'containers/TopNav/TopNavPopover';

import './TopNavDesktopItems.scss';

const getStartedPopoverItems: TopNavPopoverItemType[] = [
  {
    description: 'Learn about Learvac',
    iconType: IconType.fileDocument,
    title: 'About Us',
    to: '/aboutus',
  },
  {
    description: 'Check out our latest course, Indian Scholastic Assesment',
    iconSize: 28,
    iconType: IconType.github,
    title: 'IND SAT',
    to: '/ind-sat',
  },
];

const morePopoverItems: TopNavPopoverItemType[] = [
  {
    description: 'Learn about our vision',
    iconType: IconType.hammerWrench,
    title: 'Vision',
    to: '/vision',
  },
  {
    description: 'Frequently asked questions',
    iconType: IconType.forum,
    title: 'FAQ',
    to: '/faq',
  },
];

const TopNavDesktopItems = () => {
  const [getStartedAnchorEl, setGetStartedAnchorEl] = useState<HTMLButtonElement | null>(null);
  const [moreAnchorEl, setMoreAnchorEl] = useState<HTMLButtonElement | null>(null);

  return (
    <>
      <TopNavPopover
        anchorEl={getStartedAnchorEl}
        buttonText="Get Started"
        className="TopNavDesktopItems__right-item"
        items={getStartedPopoverItems}
        popoverId="get-started-popover"
        setAnchorEl={setGetStartedAnchorEl}
      />
      <TopNavPopover
        anchorEl={moreAnchorEl}
        buttonText="More"
        className="TopNavDesktopItems__right-item"
        items={morePopoverItems}
        popoverId="more-popover"
        setAnchorEl={setMoreAnchorEl}
      />
      <div className="TopNavDesktopItems__separator" />
      <Link className="TopNavDesktopItems__right-item TopNavDesktopItems__download-button" tabIndex={-1} to="/download">
        <Button>Download</Button>
      </Link>
    </>
  );
};

export default TopNavDesktopItems;
