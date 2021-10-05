import React, {
    forwardRef,
    HTMLAttributes,
    ReactNode,
    useCallback,
    useMemo,
} from 'react';
import clsx from 'clsx';
import { bemify } from '../../../utils/bemify';

import AccountGroupIcon from 'mdi-react/AccountGroupIcon';
import AlertCircleCheckOutlineIcon from 'mdi-react/AlertCircleCheckOutlineIcon';
import AlertCircleIcon from 'mdi-react/AlertCircleIcon';
import AlertCircleOutlineIcon from 'mdi-react/AlertCircleOutlineIcon';
import AlertIcon from 'mdi-react/AlertIcon';
import ArrowCollapseDownIcon from 'mdi-react/ArrowCollapseDownIcon';
import ArrowDownIcon from 'mdi-react/ArrowDownIcon';
import ArrowLeftIcon from 'mdi-react/ArrowLeftIcon';
import ArrowRightIcon from 'mdi-react/ArrowRightIcon';
import ArrowUpIcon from 'mdi-react/ArrowUpIcon';
import BellIcon from 'mdi-react/BellIcon';
import ChartAreasplineIcon from 'mdi-react/ChartAreasplineIcon';
import ChartTimelineVariantShimmer from 'mdi-react/ChartTimelineVariantShimmerIcon';
import CheckCircleIcon from 'mdi-react/CheckCircleIcon';
import CheckboxBlankCircleIcon from 'mdi-react/CheckboxBlankCircleIcon';
import CheckboxBlankCircleOutlineIcon from 'mdi-react/CheckboxBlankCircleOutlineIcon';
import CheckboxBlankOutlineIcon from 'mdi-react/CheckboxBlankOutlineIcon';
import CheckboxMarkedIcon from 'mdi-react/CheckboxMarkedIcon';
import ChevronDownIcon from 'mdi-react/ChevronDownIcon';
import ChevronLeftIcon from 'mdi-react/ChevronLeftIcon';
import ChevronRightIcon from 'mdi-react/ChevronRightIcon';
import ChevronUpIcon from 'mdi-react/ChevronUpIcon';
import CloseIcon from 'mdi-react/CloseIcon';
import ContentCopyIcon from 'mdi-react/ContentCopyIcon';
import CurrencyUsdIcon from 'mdi-react/CurrencyUsdIcon';
import DevToIcon from 'mdi-react/DevToIcon';
import DiscordIcon from 'mdi-react/DiscordIcon';
import DotsVerticalIcon from 'mdi-react/DotsVerticalIcon';
import DownloadIcon from 'mdi-react/DownloadIcon';
import EarthIcon from 'mdi-react/EarthIcon';
import EyeIcon from 'mdi-react/EyeIcon';
import EyeOffIcon from 'mdi-react/EyeOffIcon';
import FacebookIcon from 'mdi-react/FacebookIcon';
import FileDocumentIcon from 'mdi-react/FileDocumentIcon';
import FileDownloadIcon from 'mdi-react/FileDownloadIcon';
import ForumIcon from 'mdi-react/ForumIcon';
import GithubIcon from 'mdi-react/GithubIcon';
import HammerWrenchIcon from 'mdi-react/HammerWrenchIcon';
import HumanHandsupIcon from 'mdi-react/HumanHandsupIcon';
import InformationIcon from 'mdi-react/InformationIcon';
import InstagramIcon from 'mdi-react/InstagramIcon';
import LanConnectIcon from 'mdi-react/LanConnectIcon';
import LanDisconnectIcon from 'mdi-react/LanDisconnectIcon';
import LinkIcon from 'mdi-react/LinkIcon';
import LinkedinIcon from 'mdi-react/LinkedinIcon';
import LoadingIcon from 'mdi-react/LoadingIcon';
import MapMarkerCheckIcon from 'mdi-react/MapMarkerCheckIcon';
import MenuIcon from 'mdi-react/MenuIcon';
import MenuRightIcon from 'mdi-react/MenuRightIcon';
import MinusIcon from 'mdi-react/MinusIcon';
import NotebookCheckOutlineIcon from 'mdi-react/NotebookCheckOutlineIcon';
import OpenInNewIcon from 'mdi-react/OpenInNewIcon';
import PencilIcon from 'mdi-react/PencilIcon';
import PinterestIcon from 'mdi-react/PinterestIcon';
import PlayBoxMultipleIcon from 'mdi-react/PlayBoxMultipleIcon';
import PlayIcon from 'mdi-react/PlayIcon';
import PlusIcon from 'mdi-react/PlusIcon';
import QrcodeIcon from 'mdi-react/QrcodeIcon';
import RadioboxBlankIcon from 'mdi-react/RadioboxBlankIcon';
import RadioboxMarkedIcon from 'mdi-react/RadioboxMarkedIcon';
import RedditIcon from 'mdi-react/RedditIcon';
import RefreshIcon from 'mdi-react/RefreshIcon';
import SlackIcon from 'mdi-react/SlackIcon';
import SortAscendingIcon from 'mdi-react/SortAscendingIcon';
import SortDescendingIcon from 'mdi-react/SortDescendingIcon';
import SyncIcon from 'mdi-react/SyncIcon';
import TextBoxIcon from 'mdi-react/TextBoxIcon';
import ThumbsUpIcon from 'mdi-react/ThumbsUpIcon';
import TrophyIcon from 'mdi-react/TrophyIcon';
import TwitchIcon from 'mdi-react/TwitchIcon';
import TwitterIcon from 'mdi-react/TwitterIcon';
import YoutubeIcon from 'mdi-react/YoutubeIcon';

import '../../styles/colors.css';
import './Icon.scss';

// These names are camelCased versions of the names found in https://materialdesignicons.com/
export enum IconType {
    accountGroup = 'account-group',
    alert = 'alert',
    alertCircle = 'alert-circle',
    alertCircleCheckOutline = 'alert-circle-check-outline',
    alertCircleOutline = 'alert-circle-outline',
    arrowCollapseDown = 'arrow-collapse-down',
    arrowDown = 'arrow-down',
    arrowLeft = 'arrow-left',
    arrowRight = 'arrow-right',
    arrowUp = 'arrow-up',
    bell = 'bell',
    chartAreaspline = 'chart-areaspline',
    chartTimelineVariantShimmer = 'chart-timeline-variant-shimmer',
    checkCircle = 'check-circle',
    checkboxBlankCircle = 'checkbox-blank-circle',
    checkboxBlankCircleOutline = 'checkbox-blank-circle-outline',
    checkboxBlankOutline = 'checkbox-blank-outline',
    checkboxMarked = 'checkbox-marked',
    chevronDown = 'chevron-down',
    chevronLeft = 'chevron-left',
    chevronRight = 'chevron-right',
    chevronUp = 'chevron-up',
    close = 'close',
    contentCopy = 'content-copy',
    currencyUsd = 'currency-usd',
    devTo = 'dev-to',
    discord = 'discord',
    dotsVertical = 'dots-vertical',
    download = 'download',
    earth = 'earth',
    eye = 'eye',
    eyeOff = 'eye-off',
    facebook = 'facebook',
    fileDocument = 'file-document',
    fileDownload = 'file-download',
    forum = 'forum',
    github = 'github',
    hammerWrench = 'hammer-wrench',
    humanHandsup = 'human-handsup',
    information = 'information',
    instagram = 'instagram',
    lanConnect = 'lan-connect',
    lanDisconnect = 'lan-disconnect',
    link = 'link',
    linkedin = 'linkedin',
    loading = 'loading',
    mapMarkerCheck = 'map-marker-check',
    menu = 'menu',
    menuRight = 'menu-right',
    minus = 'minus',
    notebookCheckOutline = 'notebook-check-outline',
    openInNew = 'open-in-new',
    pencil = 'pencil',
    pinterest = 'pinterest',
    play = 'play',
    playBoxMultiple = 'playBoxMultiple',
    plus = 'plus',
    qrcode = 'qrcode',
    radioboxBlank = 'radiobox-blank',
    radioboxMarked = 'radiobox-marked',
    reddit = 'reddit',
    refresh = 'refresh',
    slack = 'slack',
    sortAscending = 'sort-ascending',
    sortDescending = 'sort-descending',
    sync = 'sync',
    textBox = 'text-box',
    thumbsUp = 'thumbs-up',
    tnb = 'tnb',
    trophy = 'trophy',
    twitch = 'twitch',
    twitter = 'twitter',
    youtube = 'youtube',
}

export interface IconProps extends HTMLAttributes<HTMLDivElement> {
    /** Optional. Extra classNames you can pass. Storybook options: black, white, primary, secondary, tertiary, alert. */
    className?: string;
    /** Optional. identifies a DOM node for testing purposes. */
    dataTestId?: string;
    /** Optional. disabled onClick event if onClick is passed. */
    disabled?: boolean;
    /** Required. pass in the icon type, using the IconType enum. */
    icon: IconType;
    /** Optional. add an onClick event handler. */
    onClick?(e?: React.MouseEvent<HTMLDivElement, MouseEvent>): void;
    /** Optional. add an onKeyDown event handler. */
    onKeyDown?(e?: React.KeyboardEvent<HTMLDivElement>): void;
    /** Optional. size of the actual icon. */
    size?: number;
    /** Optional. size of the icon + paddings. Ignored if value is smaller than size.  */
    totalSize?: number | 'unset';
    /** Optional. disables focus. Only works if there is also an onClick handler.  */
    unfocusable?: boolean;
}

/**
 * Icon component with optional ability to pass in an onClick event handler.
 */
const Icon = forwardRef<HTMLDivElement, IconProps>(
    (
        {
            className,
            dataTestId,
            disabled = false,
            icon,
            onClick,
            onKeyDown,
            size,
            totalSize = 30,
            unfocusable = false,
        },
        ref
    ) => {
        const divStyle = useMemo(() => {
            if (totalSize === 'unset') return {};
            const divSize = Math.max(size || 0, totalSize);
            return { height: divSize, width: divSize };
        }, [size, totalSize]);

        const tabIndex = useMemo(
            () => (unfocusable || disabled || !onClick ? undefined : 0),
            [disabled, onClick, unfocusable]
        );

        const handleClick = (
            e?: React.MouseEvent<HTMLDivElement, MouseEvent>
        ): void => {
            if (disabled || !onClick) return;

            onClick(e);
        };

        const handleKeyDown = (e: React.KeyboardEvent<HTMLDivElement>): void => {
            if (!onClick) return;

            if (e.key === 'Enter' && !disabled) {
                handleClick();
            }

            onKeyDown?.(e);
        };

        const renderIcon = useCallback((): ReactNode => {
            const iconBaseProps = {
                'data-testid': 'Icon__svg',
            };

            switch (icon) {
                case IconType.accountGroup:
                    return <AccountGroupIcon {...iconBaseProps} size={size || 24} />;
                case IconType.alert:
                    return <AlertIcon {...iconBaseProps} size={size || 24} />;
                case IconType.alertCircleCheckOutline:
                    return (
                        <AlertCircleCheckOutlineIcon {...iconBaseProps} size={size || 24} />
                    );
                case IconType.alertCircle:
                    return <AlertCircleIcon {...iconBaseProps} size={size || 24} />;
                case IconType.alertCircleOutline:
                    return (
                        <AlertCircleOutlineIcon {...iconBaseProps} size={size || 24} />
                    );
                case IconType.arrowCollapseDown:
                    return <ArrowCollapseDownIcon {...iconBaseProps} size={size || 22} />;
                case IconType.arrowDown:
                    return <ArrowDownIcon {...iconBaseProps} size={size || 24} />;
                case IconType.arrowLeft:
                    return <ArrowLeftIcon {...iconBaseProps} size={size || 24} />;
                case IconType.arrowRight:
                    return <ArrowRightIcon {...iconBaseProps} size={size || 24} />;
                case IconType.arrowUp:
                    return <ArrowUpIcon {...iconBaseProps} size={size || 24} />;
                case IconType.bell:
                    return <BellIcon {...iconBaseProps} size={size || 22} />;
                case IconType.chartAreaspline:
                    return <ChartAreasplineIcon {...iconBaseProps} size={size || 24} />;
                case IconType.chartTimelineVariantShimmer:
                    return (
                        <ChartTimelineVariantShimmer {...iconBaseProps} size={size || 24} />
                    );
                case IconType.checkCircle:
                    return <CheckCircleIcon {...iconBaseProps} size={size || 24} />;
                case IconType.checkboxBlankCircle:
                    return (
                        <CheckboxBlankCircleIcon {...iconBaseProps} size={size || 24} />
                    );
                case IconType.checkboxBlankCircleOutline:
                    return (
                        <CheckboxBlankCircleOutlineIcon
                            {...iconBaseProps}
                            size={size || 24}
                        />
                    );
                case IconType.checkboxBlankOutline:
                    return (
                        <CheckboxBlankOutlineIcon {...iconBaseProps} size={size || 24} />
                    );
                case IconType.checkboxMarked:
                    return <CheckboxMarkedIcon {...iconBaseProps} size={size || 24} />;
                case IconType.chevronDown:
                    return <ChevronDownIcon {...iconBaseProps} size={size || 24} />;
                case IconType.chevronLeft:
                    return <ChevronLeftIcon {...iconBaseProps} size={size || 24} />;
                case IconType.chevronRight:
                    return <ChevronRightIcon {...iconBaseProps} size={size || 24} />;
                case IconType.chevronUp:
                    return <ChevronUpIcon {...iconBaseProps} size={size || 24} />;
                case IconType.close:
                    return <CloseIcon {...iconBaseProps} size={size || 24} />;
                case IconType.contentCopy:
                    return <ContentCopyIcon {...iconBaseProps} size={size || 22} />;
                case IconType.currencyUsd:
                    return <CurrencyUsdIcon {...iconBaseProps} size={size || 24} />;
                case IconType.devTo:
                    return <DevToIcon {...iconBaseProps} size={size || 24} />;
                case IconType.discord:
                    return <DiscordIcon {...iconBaseProps} size={size || 20} />;
                case IconType.dotsVertical:
                    return <DotsVerticalIcon {...iconBaseProps} size={size || 24} />;
                case IconType.download:
                    return <DownloadIcon {...iconBaseProps} size={size || 24} />;
                case IconType.earth:
                    return <EarthIcon {...iconBaseProps} size={size || 24} />;
                case IconType.eye:
                    return <EyeIcon {...iconBaseProps} size={size || 22} />;
                case IconType.eyeOff:
                    return <EyeOffIcon {...iconBaseProps} size={size || 22} />;
                case IconType.facebook:
                    return <FacebookIcon {...iconBaseProps} size={size || 24} />;
                case IconType.fileDocument:
                    return <FileDocumentIcon {...iconBaseProps} size={size || 24} />;
                case IconType.fileDownload:
                    return <FileDownloadIcon {...iconBaseProps} size={size || 24} />;
                case IconType.forum:
                    return <ForumIcon {...iconBaseProps} size={size || 24} />;
                case IconType.github:
                    return <GithubIcon {...iconBaseProps} size={size || 24} />;
                case IconType.hammerWrench:
                    return <HammerWrenchIcon {...iconBaseProps} size={size || 24} />;
                case IconType.humanHandsup:
                    return <HumanHandsupIcon {...iconBaseProps} size={size || 24} />;
                case IconType.information:
                    return <InformationIcon {...iconBaseProps} size={size || 24} />;
                case IconType.instagram:
                    return <InstagramIcon {...iconBaseProps} size={size || 24} />;
                case IconType.lanConnect:
                    return <LanConnectIcon {...iconBaseProps} size={size || 24} />;
                case IconType.lanDisconnect:
                    return <LanDisconnectIcon {...iconBaseProps} size={size || 24} />;
                case IconType.link:
                    return <LinkIcon {...iconBaseProps} size={size || 24} />;
                case IconType.linkedin:
                    return <LinkedinIcon {...iconBaseProps} size={size || 24} />;
                case IconType.loading:
                    return <LoadingIcon {...iconBaseProps} size={size || 24} />;
                case IconType.mapMarkerCheck:
                    return <MapMarkerCheckIcon {...iconBaseProps} size={size || 24} />;
                case IconType.menu:
                    return <MenuIcon {...iconBaseProps} size={size || 24} />;
                case IconType.menuRight:
                    return <MenuRightIcon {...iconBaseProps} size={size || 24} />;
                case IconType.minus:
                    return <MinusIcon {...iconBaseProps} size={size || 24} />;
                case IconType.notebookCheckOutline:
                    return (
                        <NotebookCheckOutlineIcon {...iconBaseProps} size={size || 24} />
                    );
                case IconType.openInNew:
                    return <OpenInNewIcon {...iconBaseProps} size={size || 24} />;
                case IconType.pencil:
                    return <PencilIcon {...iconBaseProps} size={size || 24} />;
                case IconType.pinterest:
                    return <PinterestIcon {...iconBaseProps} size={size || 24} />;
                case IconType.play:
                    return <PlayIcon {...iconBaseProps} size={size || 24} />;
                case IconType.playBoxMultiple:
                    return <PlayBoxMultipleIcon {...iconBaseProps} size={size || 24} />;
                case IconType.plus:
                    return <PlusIcon {...iconBaseProps} size={size || 24} />;
                case IconType.qrcode:
                    return <QrcodeIcon {...iconBaseProps} size={size || 24} />;
                case IconType.radioboxBlank:
                    return <RadioboxBlankIcon {...iconBaseProps} size={size || 24} />;
                case IconType.radioboxMarked:
                    return <RadioboxMarkedIcon {...iconBaseProps} size={size || 24} />;
                case IconType.reddit:
                    return <RedditIcon {...iconBaseProps} size={size || 24} />;
                case IconType.refresh:
                    return <RefreshIcon {...iconBaseProps} size={size || 24} />;
                case IconType.slack:
                    return <SlackIcon {...iconBaseProps} size={size || 24} />;
                case IconType.sortAscending:
                    return <SortAscendingIcon {...iconBaseProps} size={size || 22} />;
                case IconType.sortDescending:
                    return <SortDescendingIcon {...iconBaseProps} size={size || 22} />;
                case IconType.sync:
                    return <SyncIcon {...iconBaseProps} size={size || 24} />;
                case IconType.textBox:
                    return <TextBoxIcon {...iconBaseProps} size={size || 20} />;
                case IconType.thumbsUp:
                    return <ThumbsUpIcon {...iconBaseProps} size={size || 20} />;
                case IconType.trophy:
                    return <TrophyIcon {...iconBaseProps} size={size || 22} />;
                case IconType.twitch:
                    return <TwitchIcon {...iconBaseProps} size={size || 24} />;
                case IconType.twitter:
                    return <TwitterIcon {...iconBaseProps} size={size || 24} />;
                case IconType.youtube:
                    return <YoutubeIcon {...iconBaseProps} size={size || 24} />;
                default:
                    return null;
            }
        }, [icon, size]);

        return (
            <div
                className={clsx('Icon', className, {
                    'Icon--button': !!onClick,
                    'Icon--disabled': disabled,
                    ...bemify(className, '--disabled', disabled),
                })}
                data-testid={dataTestId || 'Icon'}
                ref={ref}
                role={!!onClick ? 'button' : 'img'}
                onClick={handleClick}
                onKeyDown={handleKeyDown}
                style={divStyle}
                tabIndex={tabIndex}
            >
                {renderIcon()}
            </div>
        );
    }
);

export { Icon };