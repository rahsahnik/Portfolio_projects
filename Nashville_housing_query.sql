-- DATA CLEANING USING SQL SERVER

select Top 100 * from Portfolio_project..NashvilleHousing ;

select saleDate,cast(saleDate as date) from Portfolio_project..NashvilleHousing;

update Portfolio_project..NashvilleHousing 
set saleDate=cast(saleDate as date);

alter table NashvilleHousing  add SaleDateConverted date;

update Portfolio_project..NashvilleHousing 
set SaleDateConverted =cast(saleDate as date); -- We can also use convert(date, saleDate)

select saleDate,SaleDateConverted from Portfolio_project..NashvilleHousing;


select count(ParcelID) as Parcel_ID,count(distinct ParcelID) as Unique_Parcel_ID, 
count(ParcelID)-count(distinct ParcelID) as Duplicate_value 
from Portfolio_project..NashvilleHousing ;

select  * from Portfolio_project..NashvilleHousing 
order by ParcelID;

Select a.ParcelID,a.PropertyAddress,b.ParcelID,b.PropertyAddress,isnull(a.PropertyAddress,b.PropertyAddress)
from Portfolio_project..NashvilleHousing a
join 
Portfolio_project..NashvilleHousing b on
a.ParcelID = b.ParcelID and 
a.[UniqueID ]<>b.[UniqueID ]
where a.PropertyAddress is null;

update a
set PropertyAddress = isnull(a.PropertyAddress,b.PropertyAddress)
from Portfolio_project..NashvilleHousing a
join 
Portfolio_project..NashvilleHousing b on
a.ParcelID = b.ParcelID and 
a.[UniqueID ]<>b.[UniqueID ]
where a.PropertyAddress is null;

select  * from Portfolio_project..NashvilleHousing 
order by ParcelID;

select PropertyAddress,SUBSTRING(PropertyAddress, 1, charindex(',',PropertyAddress) -1 ) ,
SUBSTRING(PropertyAddress,charindex(',',PropertyAddress) +1 ,len(PropertyAddress))
from Portfolio_project..NashvilleHousing;

alter table NashvilleHousing  add PropertySplitAddress nvarchar(255);

update Portfolio_project..NashvilleHousing 
set PropertySplitAddress =SUBSTRING(PropertyAddress, 1, charindex(',',PropertyAddress) -1 );

alter table NashvilleHousing  add PropertySplitCity nvarchar(255);

update Portfolio_project..NashvilleHousing 
set PropertySplitCity = SUBSTRING(PropertyAddress,charindex(',',PropertyAddress) +1 ,len(PropertyAddress));

select  * from Portfolio_project..NashvilleHousing 
order by ParcelID;

--Another way of splitting the Substring : using "PARSENAME" -> splits string on ".".
--converting the commas to periods. Also indexing is done in reverse 
select 
parsename(replace(OwnerAddress,',','.'),3),
parsename(replace(OwnerAddress,',','.'),2),
parsename(replace(OwnerAddress,',','.'),1)
from Portfolio_project..NashvilleHousing ;

alter table NashvilleHousing  add OwnerSplitAddress nvarchar(255);

update Portfolio_project..NashvilleHousing 
set OwnerSplitAddress =parsename(replace(OwnerAddress,',','.'),3);

alter table NashvilleHousing  add OwnerSplitCity nvarchar(255);

update Portfolio_project..NashvilleHousing 
set OwnerSplitCity = parsename(replace(OwnerAddress,',','.'),2);

alter table NashvilleHousing  add OwnerSplitState nvarchar(255);

update Portfolio_project..NashvilleHousing 
set OwnerSplitState = parsename(replace(OwnerAddress,',','.'),1);

select  * from Portfolio_project..NashvilleHousing 
order by ParcelID;

select  distinct(SoldAsVacant) , count(SoldAsVacant)
from  Portfolio_project..NashvilleHousing 
group by SoldAsVacant
order by 2;

select SoldAsVacant,
case when SoldAsVacant='Y' then 'Yes'
	when SoldAsVacant ='N' then 'No'
	else SoldAsVacant
	end
from Portfolio_project..NashvilleHousing ;

update Portfolio_project..NashvilleHousing 
set SoldAsVacant=case when SoldAsVacant='Y' then 'Yes'
	when SoldAsVacant ='N' then 'No'
	else SoldAsVacant
	end;



select *,
	ROW_NUMBER() over(
	partition by ParcelID ,
				  PropertyAddress,
				 SalePrice,
				 SaleDate,
				 LegalReference
				 ORDER BY  UniqueID  ) as row_num
From Portfolio_Project.dbo.NashvilleHousing
order by ParcelID


with RowNumberCTE as(
select *,
	ROW_NUMBER() over(
	partition by ParcelID ,
				  PropertyAddress,
				 SalePrice,
				 SaleDate,
				 LegalReference
				 ORDER BY  UniqueID  ) as row_num
From Portfolio_Project.dbo.NashvilleHousing
--order by ParcelID
)

select * from RowNumberCTE where row_num > 1 Order by PropertyAddress

-- To delete duplicate data
--delete from RowNumberCTE where row_num > 1  


-- Delete Unused Columns
Select *
From Portfolio_Project.dbo.NashvilleHousing


ALTER TABLE Portfolio_Project.dbo.NashvilleHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate